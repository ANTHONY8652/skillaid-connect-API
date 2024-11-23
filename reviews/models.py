from django.db import models
from course.models import Course
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Review(models.Model):
    course_title = models.CharField(max_length=100)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    review_content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.course_title} - {self.rating}'
    
    class Meta:
        ordering = ['created_at']
        verbose_name = 'Course Review'
        verbose_name = 'Course Reviews'


# Create your models here.
