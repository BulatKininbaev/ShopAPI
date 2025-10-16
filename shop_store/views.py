from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница."""
    return HttpResponse('<h1>Hello, магазин продаж?</h1>')


def about(request):
    """Страница о нас."""
    return HttpResponse('<h1>О нас</h1>')

