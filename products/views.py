from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    
    # Pagination - 10 products per page
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    context = {
        'category': category,
        'products': products,
        'categories': categories
    }
    return render(request, 'products/product_list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)