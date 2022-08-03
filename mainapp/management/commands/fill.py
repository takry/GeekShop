import json
from django.conf import settings
from django.core.management import BaseCommand

from authapp.models import ShopUser
from mainapp.models import Category, Product


class Command(BaseCommand):
    @staticmethod
    def _load_data_from_file(file_name):
        with open(f'{settings.BASE_DIR}/mainapp/json/{file_name}.json') as json_file:
            return json.load(json_file)

    def handle(self, *args, **options):
        Category.objects.all().delete()
        categories_list = self._load_data_from_file('categories')
        print(categories_list)
        categories_batch = []
        for cat in categories_list:
            categories_batch.append(
                Category(
                    name=cat['name'],
                    description=cat['description'],
                )
            )
        Category.objects.bulk_create(categories_batch)
        Product.objects.all().delete()
        products_list = self._load_data_from_file('products')
        for prod in products_list:
            _cat = Category.objects.filter(name=prod.get('category')).first()
            prod['category'] = _cat
            Product.objects.create(**prod)
        shop_user = ShopUser.objects.create_superuser(username='django', email='django@bg.local', age=31)
        shop_user.set_password('geekbrains')
        shop_user.save()
