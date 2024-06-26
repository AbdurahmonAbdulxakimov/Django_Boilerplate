# Generated by Django 4.2.2 on 2024-02-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0021_headerad'),
    ]

    operations = [
        migrations.AddField(
            model_name='basead',
            name='expire_date',
            field=models.DateField(blank=True, null=True, verbose_name='expire date'),
        ),
        migrations.AddField(
            model_name='basead',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='headerad',
            name='expire_date',
            field=models.DateField(blank=True, null=True, verbose_name='expire date'),
        ),
        migrations.AddField(
            model_name='headerad',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='mainad',
            name='expire_date',
            field=models.DateField(blank=True, null=True, verbose_name='expire date'),
        ),
        migrations.AddField(
            model_name='mainad',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='singlead',
            name='expire_date',
            field=models.DateField(blank=True, null=True, verbose_name='expire date'),
        ),
        migrations.AddField(
            model_name='singlead',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
        migrations.AddField(
            model_name='timelinead',
            name='expire_date',
            field=models.DateField(blank=True, null=True, verbose_name='expire date'),
        ),
        migrations.AddField(
            model_name='timelinead',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='is active'),
        ),
    ]
