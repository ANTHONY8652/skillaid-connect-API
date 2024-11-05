from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.__db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [
        ('Staff', 'Staff'),
        ('Instructor', 'Instructor'),
        ('Student', 'Student')
    ]
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True)
    role = models.CharField(max_length=14, choices=ROLE_CHOICES, default='Student')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name = 'custom_user_groups',
        blank = True,
        help_text = 'The groups this user belongs to.',
        verbose_name = 'groups'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name = 'custom_user_permissions',
        blank = True,
        help_text = 'Specific permissions for this user.',
        verbose_name = 'user permissions',
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    class Meta:
        permissions = [
            ('can_view_courses', 'Can view available courses'),
            ('can_edit_courses', 'Can edit course content'),
            ('can_manage_users', 'Can manage user accounts'),

        ]

    def __str__(self):
        return self.email
    


# Create your models here.
