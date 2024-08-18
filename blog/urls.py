from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostCreateView1,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('home/', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<slug:slug>/', views.meetingDetail, name='meeting_detail'),
    path('post/<slug:slug>/discussions', views.discussions, name='discussions'),
    path('about/', views.about, name='blog-about'),
    path('', views.index, name='blog-index'),
    path('feedback/', views.PostCreateView1.as_view(), name='feedback'),
    path('Meetings/', views.meeting, name='meeting'),
    path('Report/', views.analysis, name='analysis'),
    
    
]