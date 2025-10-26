import pytest
from shop_store.models import Category
from django.test import Client
from django.urls import reverse


@pytest.mark.django_db
def test_view_create():
    """Тест с view и urls"""
    client = Client()
    prod_category = Category.objects.create(name='Бытовая техника',description='Все для дома')
    response = client.post(reverse('product_add',kwargs={'category_id': prod_category.id}), {'name': 'Утюг', 'price': 300.35,'description':'Все для дома','category_id':prod_category.id})
    assert response.status_code == 200
    assert 'Утюг' in response.content.decode()
