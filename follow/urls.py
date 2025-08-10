from django.urls import path
from . import views

app_name = 'follow'  # ✅ додає неймспейс до всіх URL

urlpatterns = [
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('followers/<str:username>/', views.followers_list, name='followers_list'),
    path('following/<str:username>/', views.following_list, name='following_list'),
    path('follow/follow/<str:username>/', views.follow_user, name='follow'),
    path('follow/unfollow/<str:username>/', views.unfollow_user, name='unfollow'),
]