# Generated by Django 3.2.9 on 2022-03-07 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0016_auto_20220307_1143'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
