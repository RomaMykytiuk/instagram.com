from django.http import JsonResponse
from .models import Post, Like
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# Create your views here.


def home_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post/home.html', {'posts': posts})

# def create_post(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Змінюй на потрібний URL
#     else:
#         form = PostForm()
#     return render(request, 'post/create_post.html', {'form': form})
#
from django.shortcuts import render, redirect
from .forms import PostForm, ImageForm

def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            image = image_form.save(commit=False)
            image.post = post
            image.save()

            return redirect('post:home')
    else:
        post_form = PostForm()
        image_form = ImageForm()

    return render(request, 'post/create_post.html', {'post_form': post_form, 'image_form': image_form})



@require_POST
@login_required
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({
        'liked': liked,
        'likes': post.like_set.count(),
    })


