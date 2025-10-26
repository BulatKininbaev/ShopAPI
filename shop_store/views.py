from django.shortcuts import render,get_object_or_404,redirect
from .models import Category,Product
from .forms import ProductModelForm,ProductDeleteForm

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
        'category_id': category_id,
        'category_name': cat_name,
        'content': prod,
    }
    return render(request, 'products.html', context=context)

def product(request,product_id):
    """ Описание товара """
    prod = get_object_or_404(Product,pk=product_id)
    context = {
        'prod': prod
    }
    return render(request, 'product.html', context=context)


def product_add(request,category_id):
    """Форма для добавления нового товара  конкретной категории. """
    if request.method == 'POST':
        form = ProductModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products',category_id)
    else:
        prod = Product()
        prod.category = Category.objects.get(pk=category_id)
        form = ProductModelForm(instance=prod)

    context = {
        'form': form,
        'title': 'Добавить товар'
    }
    return render(request, 'product_add.html', context=context)

def product_edit(request,product_id):
    """Форма для редактирования товара . """
    prod = get_object_or_404(Product,pk=product_id)
    category_id=prod.category.pk
    if request.method == 'POST':
        form = ProductModelForm(request.POST,instance=prod)
        if form.is_valid():
            form.save()
            return redirect('products',category_id)
    else:
        form = ProductModelForm(instance=prod)

    context = {
        'form': form,
        'title': 'Редактировать товар'
    }
    return render(request, 'product_edit.html', context=context)

def product_delete(request,product_id):
    """Форма для удаления товара . """
    prod = get_object_or_404(Product,pk=product_id)
    category_id=prod.category.pk

    if request.method == 'POST':
        form = ProductDeleteForm(request.POST)
        if form.is_valid() and form.cleaned_data['confirm']:
            prod.delete()
            return redirect('products',category_id)
    else:
        form = ProductDeleteForm()

    context = {
        'form': form,
        'prod': prod,
        'title': 'Удалить товар'
    }
    return render(request, 'product_delete.html', context=context)



def about(request):
    """Страница о нас."""
    return render(request, 'about.html')

