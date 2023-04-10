from django.urls import path
from .views import HomePageView,DetailPageView, PostCreateView,PostUpdateView,PostDeleteView, RegisterView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('post/<int:id>/', DetailPageView.as_view(), name='post_detail'),
    path('post/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(),name='post_delete'),
    path('posts/register/', RegisterView.as_view(), name='register'),
    
]
    

