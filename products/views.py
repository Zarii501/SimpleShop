from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import *
import random
from django.http import JsonResponse
from rag.service import ask
import json
from django.views.decorators.csrf import csrf_exempt
import subprocess
import sys
from django.http import JsonResponse

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    products = list(products)
    random.shuffle(products)
    
    # Pagination - 10 products per page
    paginator = Paginator(products, 12)
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


def chat(request):

    question = request.GET.get("question", "")

    if question == "":
        return JsonResponse(
            {
                "answer": "لطفاً سؤال خود را وارد کنید."
            }
        )

    answer = ask(question)

    return JsonResponse(
        {
            "answer": answer
        }
    )


@csrf_exempt
def chat_api(request):

    if request.method == "POST":

        data = json.loads(request.body)

        question = data.get("question")

        answer = ask(question)

        return JsonResponse({
            "answer": answer
        })

    return JsonResponse({
        "answer": "درخواست نامعتبر"
    })
