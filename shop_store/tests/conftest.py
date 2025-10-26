import pytest
from shop_store.models  import Product,Category


@pytest.fixture
def prod_full():
    """полностью заполненный товар"""
    prod_cat = Category.objects.create(name='Бытовая техника',description='Все для дома')
    return Product.objects.create(name='Утюг',price=658.24,category_id=prod_cat.id,description='Отглажу все')

