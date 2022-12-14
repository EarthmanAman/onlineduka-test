# Generated by Django 2.2.5 on 2019-10-23 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_prod_keywords'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
