# Generated by Django 4.0.5 on 2022-08-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0019_marketplace_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marketplace',
            name='product_price',
            field=models.CharField(max_length=20, verbose_name='Price'),
        ),
    ]