# Generated by Django 3.2.9 on 2022-03-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0014_auto_20220307_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='contact',
            field=models.CharField(default='', max_length=10),
        ),
    ]