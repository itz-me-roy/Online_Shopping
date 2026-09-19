from django.core.management.base import BaseCommand
from django.utils.text import slugify

from shop.models import Category, Product

SAMPLE = {
    'Electronics': [
        ('Wireless Headphones', 79.99, 25),
        ('Mechanical Keyboard', 109.00, 15),
        ('4K Webcam', 59.50, 30),
    ],
    'Home & Kitchen': [
        ('Ceramic Coffee Mug', 12.00, 50),
        ('Stainless Steel Water Bottle', 18.75, 40),
        ('Non-stick Frying Pan', 34.99, 0),
    ],
    'Books': [
        ('Learning Django', 39.99, 20),
        ('Python Crash Course', 29.99, 12),
    ],
}


class Command(BaseCommand):
    help = 'Populate the database with a few sample categories and products.'

    def handle(self, *args, **options):
        created_products = 0
        for category_name, products in SAMPLE.items():
            category, _ = Category.objects.get_or_create(
                name=category_name, defaults={'slug': slugify(category_name)}
            )
            for name, price, stock in products:
                _, created = Product.objects.get_or_create(
                    name=name,
                    defaults={
                        'slug': slugify(name),
                        'category': category,
                        'price': price,
                        'stock': stock,
                        'description': f'A great {name.lower()}.',
                    },
                )
                if created:
                    created_products += 1

        self.stdout.write(self.style.SUCCESS(
            f'Done. Created {created_products} new sample product(s).'
        ))
