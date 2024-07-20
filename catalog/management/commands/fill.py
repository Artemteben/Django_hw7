import json
import os.path

from django.core.management import BaseCommand

from catalog.models import Product, Category
from django.conf import settings


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        path_cat = os.path.join(settings.BASE_DIR, 'catalog/fixtures/category.json')
        with open(path_cat, encoding='UTF-8') as file:
            lcat = json.load(file)
        return lcat

    # Здесь мы получаем данные из фикстурв с категориями

    @staticmethod
    def json_read_products():
        path_prod = os.path.join(settings.BASE_DIR, 'catalog/fixtures/product.json')
        with open(path_prod, encoding='UTF-8') as file:
            lprod = json.load(file)
        return lprod

    # Здесь мы получаем данные из фикстурв с продуктами

    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()
        # Удалите все категории

        # Создайте списки для хранения объектов
        product_for_create = []
        category_for_create = []

        # Обходим все значения категорий из фиктсуры для получения информации об одном объекте
        for i in Command.json_read_categories():
            category_for_create.append(
                Category(name=i['fields']['name']),
                description=i['fields']['description']
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(product_for_create)

        # Обходим все значения продуктов из фиктсуры для получения информации об одном объекте
        for j in Command.json_read_products():
            product_for_create.append(
                Product(name=j['fields']['name']),
                description=j['fields']['description'],
                image=j.get('fileds').get('image', 'no photo'),
                category=Category.objects.get(pk=i["pk"]),
                price=j['fields']['category'],
                created_at=j['fields']['created_at'],
                updated_at=j['fields']['updated_at']

            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Product.objects.bulk_create(product_for_create)
