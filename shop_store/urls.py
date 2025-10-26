from django.urls import path
from .views import index, about,products,product,product_add,product_edit,product_delete

urlpatterns = [
    path('index', index,name='index'),
    path('products/<int:category_id>', products,name='products'),
    path('product/<int:product_id>', product,name='product'),
    path('product/add/<int:category_id>', product_add, name='product_add'),
    path('product/edit/<int:product_id>', product_edit, name='product_edit'),
    path('product/delete/<int:product_id>', product_delete, name='product_delete'),
    path('about/', about, name='about'),
]