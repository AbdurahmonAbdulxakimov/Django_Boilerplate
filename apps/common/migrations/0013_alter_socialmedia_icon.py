# Generated by Django 4.2.2 on 2023-07-14 06:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0012_alter_socialmedia_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='icon',
            field=models.FileField(null=True, upload_to='', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['svg'])], verbose_name='icon'),
        ),
    ]