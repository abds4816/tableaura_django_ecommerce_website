from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator

# Create your views here.

def products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'products': page_obj
    }
    return render(request, 'products/products.html', context)

def categories(request):
    categories = Category.objects.all().order_by('-id')
    paginator = Paginator(categories, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'categories': page_obj
    }
    return render(request, 'products/categories.html', context)

def category(request, cat_id):
    category = get_object_or_404(Category, pk=cat_id)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'products/products.html', context)

def product(request, pro_id):
    product = get_object_or_404(Product, pk=pro_id)
    product.views += 1
    product.save()
    other_products = Product.objects.filter(category=product.category)
    related_products = []
    for pro in other_products:
        if pro.id != product.id:
            related_products.append(pro)
    context = {
        'pro': product,
        'related_products': related_products
    }
    return render(request, 'products/product.html', context)