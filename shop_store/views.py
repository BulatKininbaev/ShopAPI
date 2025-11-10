from django.shortcuts import render,get_object_or_404,redirect
from django.template.context_processors import request

from .models import Category,Product
from .forms import ProductModelForm,ProductDeleteForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from .tasks import log_new_product

def index(request):
    """Главная страница. С возвратом каталога товаров мне нужна именно не как CVB """
    category = Category.objects.all()
    context = {
        'content': category,
    }
    return render(request, 'index.html', context=context)

def about(request):
    """Страница о нас."""
    return render(request, 'about.html')


class ProductListView(ListView):
    """CVB список товаров"""
    model = Product

    template_name = 'products.html'
    context_object_name = 'content'

    def get_queryset(self):
        category_id=self.kwargs['category_id']
        queryset = super().get_queryset()

        return queryset.filter(category_id=category_id)

    def get_context_data(self, **kwargs):
        category_id=self.kwargs['category_id']
        context = super().get_context_data(**kwargs)
        context['category_name'] = Category.objects.get(pk=category_id)
        context['category_id'] = category_id
        return context


class ProductDetailView(DetailView):
    """ CVB информация о товаре. Использую минимальный набор свойcтв только для отображения """
    model = Product

    template_name = 'product.html'
    context_object_name = 'prod'


class ProductCreateView(CreateView):
    model = Product

    template_name = 'product_add.html'
    context_object_name = 'content'
    form_class = ProductModelForm
#    success_url = reverse_lazy('products',kwargs={'param': request})


    def get(self, request, *args, **kwargs):
        """Добавление с параметром по умолчанию в категорию из меню"""
        category_id = self.kwargs['category_id']
        prod = Product()
        prod.category = Category.objects.get(pk=category_id)
        form = ProductModelForm(instance=prod)
        context = {
                 'form': form,
                 'title': 'Добавить товар'
             }
        return render(request, 'product_add.html', context)

    def get_success_url(self, **kwargs):
        """Возврат в список в категорию из меню"""
        return reverse('products',kwargs = self.kwargs)

    def form_valid(self, form):
        """Сообщение об успешном создании товара"""
        messages.success(self.request, 'Товар успешно создан')
        log_new_product(form.name)
        return super().form_valid(form)



class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product_edit.html'
    form_class = ProductModelForm

    def form_valid(self, form):
        """Добавляем сообщение об успешном обновлении товара."""
        messages.success(self.request, 'Товар успешно обновлен')
        return super().form_valid(form)

    def get_success_url(self, **kwargs):
        """Возврат в список в категорию из меню"""
        prod_id = self.kwargs['pk']
        prod = get_object_or_404(Product,pk=prod_id)
        category_id=prod.category.pk
        return reverse('products',kwargs ={'category_id':category_id})


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_delete.html'

    def get_success_url(self, **kwargs):
        """Возврат в список в категорию из меню"""
        prod_id = self.kwargs['pk']
        prod = get_object_or_404(Product,pk=prod_id)
        category_id=prod.category.pk
        return reverse('products',kwargs ={'category_id':category_id})

    def form_valid(self, form):
        """Добавляем сообщение об успешном обновлении товара."""
        messages.success(self.request, 'Товар успешно удален')
        return super().form_valid(form)


# def product_add(request,category_id):
#     """Форма для добавления нового товара  конкретной категории. """
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('products',category_id)
#     else:
#         prod = Product()
#         prod.category = Category.objects.get(pk=category_id)
#         form = ProductModelForm(instance=prod)
#
#     context = {
#         'form': form,
#         'title': 'Добавить товар'
#     }
#     return render(request, 'product_add.html', context=context)

# def product_edit(request,product_id):
#     """Форма для редактирования товара . """
#     prod = get_object_or_404(Product,pk=product_id)
#     category_id=prod.category.pk
#     if request.method == 'POST':
#         form = ProductModelForm(request.POST,instance=prod)
#         if form.is_valid():
#             form.save()
#             return redirect('products',category_id)
#     else:
#         form = ProductModelForm(instance=prod)
#
#     context = {
#         'form': form,
#         'title': 'Редактировать товар'
#     }
#     return render(request, 'product_edit.html', context=context)
#
# def product_delete(request,product_id):
#     """Форма для удаления товара . """
#     prod = get_object_or_404(Product,pk=product_id)
#     category_id=prod.category.pk
#
#     if request.method == 'POST':
#         form = ProductDeleteForm(request.POST)
#         if form.is_valid() and form.cleaned_data['confirm']:
#             prod.delete()
#             return redirect('products',category_id)
#     else:
#         form = ProductDeleteForm()
#
#     context = {
#         'form': form,
#         'prod': prod,
#         'title': 'Удалить товар'
#     }
#     return render(request, 'product_delete.html', context=context)





# def products(request,category_id):
#     """Товары по выбранному каталогу"""
#     prod = Product.objects.filter(category_id=category_id)
#     cat_name = Category.objects.get(pk=category_id)
#     context = {
#         'category_id': category_id,
#         'category_name': cat_name,
#         'content': prod,
#     }
#     return render(request, 'products.html', context=context)

# def product(request,product_id):
#     """ Описание товара """
#     prod = get_object_or_404(Product,pk=product_id)
#     context = {
#         'prod': prod
#     }
#     return render(request, 'product.html', context=context)
