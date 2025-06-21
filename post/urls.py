from django.urls import path
from . import views

app_name = 'post'
urlpatterns = [
    path('',views.home_view,name='home'),
    path('create/',views.create_post,name='create_post'),
    path('like/<int:post_id>/', views.toggle_like, name='toggle_like'),
]




