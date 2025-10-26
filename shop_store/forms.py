from django import forms
from django.core.exceptions import ValidationError


from .models import Category,Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']
        labels = {
            'name': 'Наименование',
            'description': 'Описание',
            'price': 'Цена',
            'category': 'Категория',
        }
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите наименование'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'row': 2, 'placeholder': 'Введите описание товара'}),
            'м': forms.NumberInput(attrs={'step': 0.25}),
        }

    def clean_name(self):
        """Кастомная валидация name."""
        name = self.cleaned_data.get('name')
        if len(name) < 10:
            raise ValidationError('Наименование должен содержать минимум 10 символов')
        return name

    def clean_price(self):
        """Кастомная валидация цена."""
        price = self.cleaned_data.get('price')
        if price < 10 or price > 10000:
            raise ValidationError('цена должна быть в диапазоне от 10$ до 10 000$')
        return price



class ProductDeleteForm(forms.Form):
    """Форма для подтверждения удаления поста."""
    confirm = forms.BooleanField(
        required=True,
        label='Подтвердите удаление',
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}),
    )
