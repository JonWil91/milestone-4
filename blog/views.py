from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import BlogPost

# Create your views here.


def all_blogs(request):
    """ A view to return the blog page """

    blogs = BlogPost.objects.all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """ A view to show individual blog posts """

    blog = get_object_or_404(BlogPost, pk=blog_id)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_details.html', context)
