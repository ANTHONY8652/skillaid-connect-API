from django.urls import path
from .views import CourseListCreateView, CourseRetrieveUpdateOrDestroyView

urlpatterns = [
    path('', CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>/', CourseRetrieveUpdateOrDestroyView.as_view(), name='course-detail'),
]