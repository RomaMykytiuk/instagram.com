from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save


def user_directory_path(instance,filename):
    return f'user_{instance.user.id}/{filename}'



# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    bio = models.CharField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to=user_directory_path,default='img/default_avatar.png')
    birth_date = models.DateTimeField(null=True,blank=True)
    location = models.CharField(blank=True,max_length=30)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return f"{self.user.username} profile"


@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_or_update_userprofile(instance,**kwargs):
    Profile.objects.update_or_create(user=instance,defaults={})




