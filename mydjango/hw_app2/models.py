from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    address = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.address} {self.phone}'


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    order_amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
