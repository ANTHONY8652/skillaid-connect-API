from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('Programming', 'Programming'),
        ('Data Science', 'Data_Science'),
        ('AI&ML', 'AI&ML'),
        ('Graphic Design', 'Graphic Design'),
        ('Arts and Crafts', 'Arts and Crafts'),
        ('Design', 'Design'),
        ('Music', 'Music'),
        ('Electrical', 'Electrical'),
    ]

    DIFFICULTY_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]

    title = models.CharField(max_length=155)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    difficulty_level = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

# Create your models here.
