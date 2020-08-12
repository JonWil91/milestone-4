from django import forms
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
