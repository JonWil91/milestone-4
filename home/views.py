from django.shortcuts import render
from products.models import Product, Category


# Create your views here.

def index(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all().order_by('-rating')[:3]
    # Filters all products in reverse order of rating and displays the first three

    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        products = products.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
