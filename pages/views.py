from django.shortcuts import render
from products.models import Product, Category

# Create your views here.

def index(request):
    context = {
        'products': Product.objects.all().order_by('-id'),
        'categories': Category.objects.all(),
        'populars': Product.objects.all().order_by('-views')
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')

def thanks(request):
    return render(request, 'pages/thanks.html')

def not_found(request, exception):
    return render(request, 'pages/404.html')