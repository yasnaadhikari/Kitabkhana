# Generated by Django 3.2.9 on 2022-03-06 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_remove_checkout_books'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Checkout',
        ),
    ]