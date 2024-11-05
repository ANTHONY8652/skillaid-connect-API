from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from .models import User

@receiver(post_save, sender=User)
def assign_permissions(sender, instance, created, **kwargs):
    if created:
        instance.user_permissions.clear()

        if instance.role == 'Student':
            view_courses_perm = Permission.objects.get(codename='can_view_courses')
            instance.user_permissions.add(view_courses_perm)

        elif instance.role == 'Instructor':
            view_courses_perm = Permission.objects.get(codename='can_view_courses')
            edit_courses_perm = Permission.objects.get(codename='can_edit_courses')
            instance.user_permissions.add(view_courses_perm, edit_courses_perm)
        
        elif instance.role == 'Admin' or (instance.role == 'Staff' and instance.is_staff):
            view_courses_perm = Permission.objects.get(codename='can_view_courses')
            edit_courses_perm = Permission.objects.get(codename='can_edit_courses')
            manage_users_perm = Permission.objects.get(codename='can_manage_users')
            instance.user_permissions.add(view_courses_perm, edit_courses_perm, manage_users_perm)

        instance.save()