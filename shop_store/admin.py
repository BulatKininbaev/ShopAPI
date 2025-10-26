import decimal

from django.contrib import admin
from .models import Category,Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    ordering = ('name',)

    fields = ('name', 'description',)

    search_fields = ('name',)
    search_help_text = 'Введите наименование'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','description','category','price',]
    ordering = ['name',]

    fields = ('name', 'description',)
    list_filter = ['category', ]

    search_fields = ['name']
    search_help_text = 'Введите наименование'

    @admin.action(description='Увеличить цену на 5 процентов')
    def inc_price(self, request, queryset):
        proc = 5
        for prod in queryset:
            prod.price += prod.price*decimal.Decimal(proc/100)
            prod.save()

    actions = [inc_price, ]