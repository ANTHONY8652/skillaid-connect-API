from django.urls import path
from .views import CourseListCreateView, CourseRetrieveUpdateOrDestroyView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('course/<int:pk>/', CourseRetrieveUpdateOrDestroyView.as_view(), name='course-detail'),
]