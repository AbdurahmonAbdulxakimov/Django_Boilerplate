# Generated by Django 4.2.2 on 2024-04-09 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_merge_20230916_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_author',
            field=models.BooleanField(default=False, verbose_name='Is Author'),
        ),
    ]
