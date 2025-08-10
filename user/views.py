from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from follow.models import Subscription
from post.models import Post
from user.models import Profile
# Create your views here.


User = get_user_model()

User = get_user_model()


def profile_view(request, username):
    profile_user = get_object_or_404(User, username=username)
    profile = get_object_or_404(Profile, user=profile_user)

    is_following = False
    if request.user.is_authenticated and request.user != profile_user:
        is_following = Subscription.objects.filter(subscriber=request.user, target=profile_user).exists()

    # Підрахунок кількостей
    followers_count = profile_user.followers_set.count()
    following_count = profile_user.following_set.count()
    posts = Post.objects.filter(author=profile_user)
    posts_count = posts.count()

    context = {
        'profile': profile,
        'profile_user': profile_user,
        'is_following': is_following,
        'followers_count': followers_count,
        'following_count': following_count,
        'posts': posts,
        'posts_count': posts_count,
    }
    return render(request, 'user/profile.html', context)


@login_required
def edit_profile_view(request,username):
    profile = get_object_or_404(Profile, user=request.user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user:profile', username=username)
    else:
        form = EditProfileForm(instance=profile)

    return render(request, 'user/edit_profile.html',{'form': form})





