# Generated by Django 4.0.6 on 2022-08-21 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ritu_web_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task1Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.URLField(verbose_name='text')),
                ('time_added', models.DateTimeField(auto_now_add=True)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ritu_web_app.players')),
            ],
        ),
    ]
