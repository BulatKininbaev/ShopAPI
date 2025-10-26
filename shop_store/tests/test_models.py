

import pytest

@pytest.mark.django_db
def test_full_create(prod_full):
    """Тест с models"""
    assert prod_full.name == 'Утюг'
    assert prod_full.category.id == 1



