# Generated by Django 4.2.2 on 2023-07-13 09:23

import django.core.validators
from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
    ]