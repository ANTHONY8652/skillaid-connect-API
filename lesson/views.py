from django.shortcuts import render
from course.models import Course
from rest_framework import generics, status, permissions
from .models import Lesson
from .serializers import LessonSerializer

class LessonListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LessonSerializer

    def get_queryset(self, request):
        course_id = self.kwargs['course_id']
        return Lesson.objects.filter(course__id=course_id, status=status.HTTP_200_OK)
    
    def perform_create(self, serializer):
        course_id = self.kwargs['course_id']
        course = Course.objects.get(id=course_id)
        serializer.save(course=course, status=status.HTTP_201_CREATED)

# Create your views here.
