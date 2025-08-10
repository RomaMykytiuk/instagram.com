from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Subscription  # заміни на свою модель фоллову

@login_required
def follow_user(request, username):
    if request.method == 'POST':
        try:
            target_user = User.objects.get(username=username)
            if target_user != request.user:
                Subscription.objects.get_or_create(follower=request.user, following=target_user)
                return JsonResponse({'status': 'followed'}, status=200)
            else:
                return JsonResponse({'error': 'Неможливо підписатися на себе'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Користувача не знайдено'}, status=404)

@login_required
def unfollow_user(request, username):
    if request.method == 'POST':
        try:
            target_user = User.objects.get(username=username)
            if target_user != request.user:
                Subscription.objects.filter(follower=request.user, following=target_user).delete()
                return JsonResponse({'status': 'unfollowed'}, status=200)
            else:
                return JsonResponse({'error': 'Неможливо відписатися від себе'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'error': 'Користувача не знайдено'}, status=404)