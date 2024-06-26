# Generated by Django 4.2.2 on 2023-07-12 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('news', models.BooleanField(default=True, verbose_name='news')),
                ('ad_1', models.BooleanField(default=True, verbose_name='ads')),
                ('article', models.BooleanField(default=True, verbose_name='article')),
                ('special_report', models.BooleanField(default=True, verbose_name='special report')),
                ('ad_2', models.BooleanField(default=True, verbose_name='ads')),
                ('photo_report', models.BooleanField(default=True, verbose_name='photo report')),
                ('podcast', models.BooleanField(default=True, verbose_name='podcast')),
                ('interview', models.BooleanField(default=True, verbose_name='interview')),
                ('ad_3', models.BooleanField(default=True, verbose_name='ads')),
                ('speaker', models.BooleanField(default=True, verbose_name='speaker')),
                ('social_network', models.BooleanField(default=True, verbose_name='social network')),
                ('discussion', models.BooleanField(default=True, verbose_name='discussion')),
            ],
            options={
                'verbose_name': 'Main settings',
                'verbose_name_plural': 'Main settings',
            },
        ),
    ]
