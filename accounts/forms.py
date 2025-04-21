from django import forms
from .models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError



class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    login = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': "email або username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "password"})
    )

    def clean(self):
        cleaned_data = super().clean()
        login_input = cleaned_data.get("login")
        password = cleaned_data.get("password")
        user = authenticate(username=login_input, password=password)
        if user is None:
            raise ValidationError('невірний username/email  або пароль')
        self.user = user
        return cleaned_data
