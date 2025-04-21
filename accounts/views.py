from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages

from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            messages.success(request, "Ви успішно Увійшли!")
            return redirect('profile')
        else: messages.error(request, "Помилка")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created!')
            return redirect('login')
        else:
            messages.error(request, "Помилка!")
    else:
        form = UserRegistrationForm()
    return render(request, "register.html", {"form": form})




