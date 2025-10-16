from django.db import models

class Product(models.Model):
    """Таблица товаров"""
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,related_name='category')

    def __str__(self):
        """Строковое представление класса"""
        return f'Товар {self.name} с ценой: {self.price}'


class Category(models.Model):
    """Таблица категорий товаров"""
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        """Строковое представление класса"""
        return f'Группа товара {self.name}'
