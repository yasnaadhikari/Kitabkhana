# Generated by Django 3.2.9 on 2022-03-06 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_alter_checkout_books'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='books',
        ),
    ]
