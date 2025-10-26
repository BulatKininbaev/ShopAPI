from django.urls import path
from .views import  index,about
from .views import ProductListView,ProductDetailView,ProductCreateView,ProductUpdateView,ProductDeleteView
urlpatterns = [
    path('index', index,name='index'),
    path('products/<int:category_id>', ProductListView.as_view(),name='products'),
    path('product/<int:pk>', ProductDetailView.as_view(),name='product'),
    path('product/add/<int:category_id>', ProductCreateView.as_view(), name='product_add'),
    path('product/edit/<int:pk>', ProductUpdateView.as_view(), name='product_edit'),
    path('product/delete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('about/', about, name='about'),
]