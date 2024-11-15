# Generated by Django 5.1.2 on 2024-10-24 14:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.cart'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='Order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.order'),
        ),
        migrations.AddField(
            model_name='products',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.collection'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='Products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.products'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.products'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='product',
            field=models.ManyToManyField(related_name='+', to='store.products'),
        ),
        migrations.AddField(
            model_name='products',
            name='promotion',
            field=models.ManyToManyField(related_name='+', to='store.promotion'),
        ),
    ]
