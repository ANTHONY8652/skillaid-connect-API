from django.urls import path
from .views import ReviewListCreateView, ReviewDetailView

urlpatterns = [
    path('', ReviewDetailView.as_view(), name='review-detail-view'),
    path('list/<int:pk>/', ReviewListCreateView.as_view(), name='review-list-create-view'),
]