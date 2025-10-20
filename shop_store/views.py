from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Product


def index(request):
    """Главная страница. С возвратом каталога товаров"""
    category = Category.objects.all()
    context = {
        'content': category,
    }
    return render(request, 'index.html', context=context)

def products(request,category_id):
    """Товары по выбранному каталогу"""
    prod = Product.objects.filter(category_id=category_id)
    cat_name = Category.objects.get(pk=category_id)
    context = {
        'category_name': cat_name,
        'content': prod,
    }
    return render(request, 'products.html', context=context)


def about(request):
    """Страница о нас."""
    return render(request, 'about.html')

