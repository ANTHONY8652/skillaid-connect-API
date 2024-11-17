from .models import Course
from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'author', 'category', 'difficulty_level', 'created_at', 'updated_at']
        read_only_fields = ['author', 'created_at', 'updated_at']