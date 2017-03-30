from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User, Admin

class CartManager(models.Manager):
    def total(self, user):
        my_cart = Product.objects.filter(cart__id = user)
        total = 0.00
        for product in my_cart:
            total = total + float(product.price)

        return total


class Product(models.Model):
    name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    picture = models.ImageField(upload_to = 'products')
    price = models.DecimalField(decimal_places = 2, max_digits = 6)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    admin = models.ForeignKey(Admin, related_name = "product")

class Cart(models.Model):
    products = models.ManyToManyField(Product, related_name = 'cart')
    user = models.OneToOneField(User)
    objects = CartManager()






# Create your models here.
