from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.db import models
from .managers import CustomUserManager

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True,)
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/',blank=True)
    password = models.CharField(max_length=100,)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username








