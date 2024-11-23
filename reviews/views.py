from django.shortcuts import render
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import generics, permissions, filters


class ReviewListCreateView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'created_at', 'updated_at', 'review_content']
    ordering = ['created_at', 'updated_at', 'review_content']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['rating', 'created_at', 'updated_at', 'review_content']
    ordering = ['created_at', 'updated_at', 'review_content']

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
    
    def perform_delete(self, serializer):
        return self.queryset.filter(user=self.request.user)

# Create your views here.
