# Generated by Django 2.2.5 on 2019-10-28 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_auto_20191028_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartprod',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]
