from django.urls import path, include
from rest_framework import routers

from . import views

# router = routers.DefaultRouter()
# router.register("post", views.PostViewSet)

urlpatterns = [
    path("<int:post_id>", views.PostManager.as_view()),
    path("", views.PostViewer.as_view()),
    path("api-auth",
         include("rest_framework.urls", namespace="rest_framework"))
    #path('', views.IndexView.as_view(), name='index'),
    #path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    #path('edit/<int:pk>/', views.edit, name='edit'),
    #path('post/', views.postview, name='post'),
    #path('delete/<int:pk>/', views.delete, name='delete'),
]
