from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'
urlpatterns = [
    path('emailsingup/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='accounts:login'), name='logout'),
]

