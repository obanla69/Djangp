from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Customer(AbstractUser):
    MEMBERSHIP_CHOICES = [
        ('B', 'Bronze'),
        ('S', 'Silver'),
        ('G', 'Gold'),
    ]
    email = models.EmailField(unique=True)
    membership = models.CharField(max_length=1, choices=MEMBERSHIP_CHOICES, default='B')
