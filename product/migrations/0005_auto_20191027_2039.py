# Generated by Django 2.2.5 on 2019-10-27 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_prod_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='prod',
            name='hotDeal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='prod',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
