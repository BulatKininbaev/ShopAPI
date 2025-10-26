import pytest
from shop_store.forms import ProductModelForm
from shop_store.models import Category


@pytest.mark.django_db
def test_prod_form():
    """Тест формы добавления продукта """

    prod_cat = Category.objects.create(name='Бытовая техника',description='Все для дома')
    form_data = {
        'name': 'Утюг',
        'pride': 3000.58,
        'description': 'Отглажу все',
        'category_id': [prod_cat.id],
    }

    form = ProductModelForm(data=form_data)
    assert not form.is_valid()