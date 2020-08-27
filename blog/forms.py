from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost, Comment


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('__all__')

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
