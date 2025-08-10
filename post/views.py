from .models import Post, Like, Tag, PostTag
from django.shortcuts import render, redirect
from .forms import PostForm, ImageForm, CommentForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Post, Like


# Create your views here.geю

@login_required
def home_view(request):
    posts = Post.objects.all().prefetch_related('images', 'comments', 'post_tags')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post:home')
    else:
        comment_form = CommentForm()

    return render(request, 'post/home.html', {
        'posts': posts,
        'comment_form': comment_form,
    })


def create_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user
            post.save()

            # Збереження тегів
            tag_string = post_form.cleaned_data.get('tags', '')
            tag_names = [t.strip() for t in tag_string.split(',') if t.strip()]
            for name in tag_names:
                tag, _ = Tag.objects.get_or_create(name=name.lower())
                PostTag.objects.create(post=post, tag=tag)

            # Збереження зображення
            image = image_form.save(commit=False)
            image.post = post
            image.save()

            return redirect('post:home')
    else:
        post_form = PostForm()
        image_form = ImageForm()
    return render(request, 'post/create_post.html', {
        'post_form': post_form,
        'image_form': image_form
    })



#
# @require_POST
# @login_required
# def like_post(request):
#     post_id = request.POST.get('post_id')
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         return JsonResponse({'error': 'Пост не знайдено'}, status=404)
#
#     liked = Like.objects.filter(user=request.user, post=post)
#     if liked.exists():
#         liked.delete()
#         is_liked = False
#     else:
#         Like.objects.create(user=request.user, post=post)
#         is_liked = True
#
#     return JsonResponse({
#         'liked': is_liked,
#         'likes_count': post.like_set.count()
#     })


@login_required
@require_POST
def like_post_ajax(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    like, created = Like.objects.get_or_create(post=post, user= request.user)
    if not created:
        like.delete()
        is_liked = False
        print('like is delete',f'{is_liked=}')
    else:
        is_liked = True
        print('like is created',f'{is_liked=}')
    return JsonResponse({
        "is_liked": is_liked,
        "likes_count": post.likes.count()
    })



