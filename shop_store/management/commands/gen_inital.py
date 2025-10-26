from django.core.management.base import BaseCommand
from faker import Faker
from shop_store.models import Category,Product
import random

class Command(BaseCommand):
    """Создание категорий и товаров - входной параметр - количество"""
    help = 'Создание товаров '

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help=u'Количество создаваемых товаров')

    def handle(self, *args, **kwargs):
        """Создаем категории товаров и сами товары """

        self.stdout.write('Начинаем генерацию  товаров...')

        # создаем категории
        categories = [{'name':'Электроника','description':'Приборы от 200 Вт'},
                      {'name':'Бытовая техника','description':'Все что помогает в доме'},
                      {'name':'Смартфоны', 'description': 'Средства связи'},
                      {'name':'Компьютерная техника', 'description': 'Играем работаем вычисляем'},
                      ]
        created_categories=[]

        for cat_name in categories:
            cat = Category.objects.create(name=cat_name['name'],description=cat_name['description'])
            created_categories.append(cat)

        self.stdout.write(f'Создали {len(created_categories)} категорий')

        # создаем товары

        fake=Faker()
        total = kwargs['total']
        created_product=[]
        for i in range(total):
            prod = Product.objects.create(name=fake.catch_phrase(),category=random.choice(created_categories),description=fake.paragraph(),price=round(random.uniform(10, 10000), 2))
            created_product.append(prod)

        self.stdout.write(f'Создали {len(created_product)} товаров')

        self.stdout.write('завершили генерацию товаров...')
