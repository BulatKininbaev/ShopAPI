from django.db import models
from django.core.validators import MinLengthValidator,MaxValueValidator,MinValueValidator

class Product(models.Model):
    """Таблица товаров"""
    name = models.CharField( max_length=100,validators=[MinLengthValidator(5)])
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2,validators=[MinValueValidator(10),MaxValueValidator(10000)])
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE,related_name='category')

    def __str__(self):
        """Строковое представление класса"""
        return f'Товар {self.name} с ценой: {self.price}'



class Category(models.Model):
    """Таблица категорий товаров"""
    name = models.CharField(max_length=50,validators=[MinLengthValidator(5)])
    description = models.TextField()

    def __str__(self):
        """Строковое представление класса"""
        return f'Группа товара {self.name}'
