from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Course
from .serializers import CourseSerializer

class CourseListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CourseRetrieveUpdateOrDestroyView(generics.RetrieveDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]

# Create your views here.
