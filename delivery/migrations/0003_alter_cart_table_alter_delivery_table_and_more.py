# Generated by Django 4.1.7 on 2023-05-31 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0002_alter_cart_user_id'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='cart',
            table='Cart',
        ),
        migrations.AlterModelTable(
            name='delivery',
            table='Delivery',
        ),
        migrations.AlterModelTable(
            name='items',
            table='Items',
        ),
    ]
