# Generated by Django 4.0.5 on 2022-08-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0020_alter_marketplace_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
