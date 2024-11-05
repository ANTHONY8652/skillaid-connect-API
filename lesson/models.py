from django.db import models
from course.models import Course

class Lesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    course = models.ForeignKey(Course, related_name='lessons', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    order = models.IntegerField(help_text='Position of this lesson within the course')

    def __str__(self):
        return f'{self.title} (Course: {self.course.title})'
# Create your models here.
