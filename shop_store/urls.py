from django.urls import path
from .views import index, about,products

urlpatterns = [
    path('index', index,name='index'),
    path('products/<int:category_id>', products,name='products'),
    path('about/', about, name='about'),
]