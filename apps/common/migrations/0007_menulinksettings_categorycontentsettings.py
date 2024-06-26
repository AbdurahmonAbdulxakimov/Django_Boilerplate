# Generated by Django 4.2.2 on 2023-07-13 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0030_interview_cover_image_optional'),
        ('common', '0006_alter_mainsettings_ad1_alter_mainsettings_ad2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuLinkSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('main', models.BooleanField(default=True, verbose_name='main')),
                ('popular', models.BooleanField(default=True, verbose_name='popular')),
                ('author_articles', models.BooleanField(default=True, verbose_name='author articles')),
                ('special_reports', models.BooleanField(default=True, verbose_name='special reports')),
                ('photo_reports', models.BooleanField(default=True, verbose_name='photo reports')),
            ],
            options={
                'verbose_name': 'Menu link settings',
                'verbose_name_plural': 'Menu link settings',
            },
        ),
        migrations.CreateModel(
            name='CategoryContentSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('on_top', models.BooleanField(default=True, verbose_name='on top')),
                ('category', models.ForeignKey(limit_choices_to={'type': 'news'}, on_delete=django.db.models.deletion.CASCADE, to='news.category', verbose_name='category')),
            ],
            options={
                'verbose_name': 'Category content settings',
                'verbose_name_plural': 'Category content settings',
            },
        ),
    ]
