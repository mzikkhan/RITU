# Generated by Django 4.0.5 on 2022-08-23 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0011_task1text_time_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task1text',
            name='time_added',
        ),
    ]
