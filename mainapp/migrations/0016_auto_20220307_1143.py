# Generated by Django 3.2.9 on 2022-03-07 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0015_checkout_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='books',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CartCheckout',
        ),
    ]