from django.urls import path
from .views import AWSTaskAPIView
urlpatterns = [
    path('create/', AWSTaskAPIView.as_view())
]