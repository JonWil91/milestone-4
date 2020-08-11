from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ('__all__')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)