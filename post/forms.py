from .models import Post, Tag, PostTag, Image
from django import forms
from .models import Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['caption']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']


class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введіть теги через кому, напр. "travel, food, sunset"',
            'class': 'comment-input'
        })
    )

    class Meta:
        model = Post
        fields = ['caption']



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(attrs={
                'placeholder': 'Напиши коментар...',
                'class': 'comment-input',
            })
        }