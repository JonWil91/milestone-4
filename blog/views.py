from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import BlogPost
from django.http import HttpResponseRedirect


# Create your views here.


def all_blogs(request):
    """ A view to return the blog page """

    blogs = BlogPost.objects.all().order_by('-post_date')

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, blog_id):
    """ A view to show individual blog posts """

    blog = get_object_or_404(BlogPost, pk=blog_id)
    total_likes = blog.total_likes

    context = {
        'blog': blog,
        'total_likes': total_likes,
    }

    return render(request, 'blog/blog_details.html', context)


def like_view(request, pk):
    blog = get_object_or_404(BlogPost, id=request.POST.get('blog_id'))
    blog.likes.add(request.user)
    return HttpResponseRedirect(reverse('blog_detail', args=[str(pk)]))
