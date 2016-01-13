from django import forms

from .models import Post, Comment


class PostModelForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
