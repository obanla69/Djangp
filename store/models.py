import uuid

from django.core.validators import MinValueValidator
from django.db import models
from django.conf import settings
from django.db.models.fields.related import OneToOneField


class Collection(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.title


class Products(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    # slug = models.SlugField(max_length=255)
    description = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    Inventory = models.PositiveSmallIntegerField()
    last_updated = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotion = models.ManyToManyField('Promotion', related_name='+')

    def __str__(self):
        return f"{self.title} {self.price}"

    class Meta:
        ordering = ['title']


class Promotion(models.Model):
    product = models.ManyToManyField(Products, related_name='+')
    discount = models.DecimalField(max_digits=6, decimal_places=2)


class Cart:
    pass


class ManyToOneField:
    pass


class OneToManyField:
    pass


class Productserializer:
    pass


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # items = Productserializer()


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(MinValueValidator)


class Order(models.Model):
    PAYMENT_STATUS = [
        ('P', 'Pending'),
        ('S', 'Success'),
        ('F', 'Failed')
    ]
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    Order = models.ForeignKey(Order, on_delete=models.PROTECT)
    Products = models.ForeignKey(Products, on_delete=models.CASCADE)


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Review(models.Model):
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    product = models.ForeignKey(Products, on_delete=models.PROTECT, related_name="reviews")
    title = models.CharField(max_length=255)
    content = models.TextField()


class CreateProductserializer:
    pass
