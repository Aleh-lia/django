from django.core.management import BaseCommand

from hw_app2.models import Client, Product, Order


class Command(BaseCommand):
    help = 'Creates'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Author ID')

    def handle(self, clients=None, products=None, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'name{i}', email=f'Client{i}@gmail.com', address=f'address{i}', phone=f'{i+2}{i}{i+1}{i}{i+1}{i}{i+3}')
            client.save()
        for j in range(1, count + 1):
            product = Product(product_name=f' product_name{j}', product_description=f'article{j}', price=f'{j+1}{j}', quantity=f'{j+1}{j}')
            product.save()
