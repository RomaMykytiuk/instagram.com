from django.urls import path
from . import views

urlpatterns = [
    path('accounts/emailsingup/', views.register, name='register'),
    path('accounts/login/', views.login_view, name='login'),
    #path('accounts/logout/',views.user_logout, name='logout'),
]