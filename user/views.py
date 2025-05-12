from django.shortcuts import render,get_object_or_404
from .models import Profile
from django.contrib.auth import get_user_model
# Create your views here.


User = get_user_model()


def profile_view(request,username):
    user = get_object_or_404(User,username=username)
    profile = get_object_or_404(Profile,user=user)
    return render(request,'user/profile.html',{'profile':profile})
