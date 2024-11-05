from django.shortcuts import render
from rest_framework import generics, status, permissions
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.response import Response
from .models import Course
from rest_framework.exceptions import PermissionDenied
from .serializers import CourseSerializer

class IsStaffOrAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff or request.user.has_perm('users.can_manage_users')
        )
    
    def has_object_permission(self, request, view, obj):
        return request.user.has_perm('users.can_edit_courses')

class CourseListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, DjangoModelPermissions]

    def get(self, request):
        if not request.user.has_perm('users.can_view_courses'):
            return Response({'error': 'permission denied'}, status=status.HTTP_403_FORBIDDEN)
        
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
    permission_classes = [permissions.IsAuthenticated, IsStaffOrAdmin]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        if not request.user.has_perm('users.can_view_courses'):
            raise PermissionDenied('You do not have permissions to view this sorry', status=status.HTTP_401_UNAUTHORIZED)
        return self.retrieve(request, *args, **kwargs)

# Create your views here.
