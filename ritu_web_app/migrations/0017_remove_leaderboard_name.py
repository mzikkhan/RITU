# Generated by Django 4.0.5 on 2022-08-25 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0016_alter_leaderboard_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='name',
        ),
    ]
