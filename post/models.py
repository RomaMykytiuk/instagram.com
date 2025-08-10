from django.db import models
from django.conf import settings



class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name='posts')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    caption = models.CharField(max_length=500)

    def __str__(self):
        return f'Post by {self.author.username}'

    @property
    def likes(self):
        return [like.user for like in self.like_set.all()]


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post','user')
    def __str__(self):
        return f'Like by {self.user.username} on post_id {self.post.id}'


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'


class Image(models.Model):
    image = models.ImageField(upload_to='posts/')
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="images")

    def __str__(self):
        return f'image for post_id {self.post.id}'


class PostTag(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="post_tags")
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name="post_tags")



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'