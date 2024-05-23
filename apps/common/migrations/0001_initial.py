# Generated by Django 4.2.1 on 2023-06-27 06:58

import ckeditor_uploader.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=100, scale=None, size=[1920, 1080], upload_to='ad/%Y/%m/%d', verbose_name='image')),
                ('link', models.URLField(verbose_name='link')),
            ],
            options={
                'verbose_name': 'Ad',
                'verbose_name_plural': 'Ads',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('icon', models.FileField(upload_to='contact/%Y/%m/%d', validators=[django.core.validators.FileExtensionValidator(['svg'])], verbose_name='icon')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('order', models.IntegerField(default=1, verbose_name='order')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ExchangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('usd', models.FloatField(default=0, verbose_name='usd')),
                ('usd_diff', models.FloatField(default=0, verbose_name='usd diff')),
                ('eur', models.FloatField(default=0, verbose_name='eur')),
                ('eur_diff', models.FloatField(default=0, verbose_name='eur diff')),
                ('rub', models.FloatField(default=0, verbose_name='rub')),
                ('rub_diff', models.FloatField(default=0, verbose_name='rub diff')),
            ],
            options={
                'verbose_name': 'Exchange rate',
                'verbose_name_plural': 'Exchange rates',
            },
        ),
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='UZ', verbose_name='phone number')),
                ('description', models.TextField(verbose_name='description')),
            ],
            options={
                'verbose_name': 'Feedback',
                'verbose_name_plural': 'Feedbacks',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('title', models.CharField(choices=[('youtube', 'youtube'), ('telegram', 'telegram'), ('instagram', 'instagram'), ('facebook', 'facebook'), ('vk', 'vk'), ('okru', 'okru'), ('twitter', 'twitter'), ('feed', 'feed')], max_length=255, verbose_name='title')),
                ('link', models.URLField(verbose_name='link')),
                ('follower_count', models.IntegerField(default=0, verbose_name='follower count')),
                ('order', models.IntegerField(default=1, verbose_name='order')),
                ('icon',  models.FileField(verbose_name='icon', null=True)),
            ],
            options={
                'verbose_name': 'Social media',
                'verbose_name_plural': 'Social media',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='StaticPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('slug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='slug')),
                ('slug_from_lang', models.CharField(blank=True, choices=[('uz', 'Uzbek'), ('ru', 'Russian')], max_length=64, null=True, verbose_name='select the language of the slug')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='content')),
                ('content_uz', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content')),
                ('content_ru', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='content')),
            ],
            options={
                'verbose_name': 'Static page',
                'verbose_name_plural': 'Static pages',
            },
        ),
        migrations.CreateModel(
            name='TimelineAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('order', models.IntegerField(default=1, verbose_name='order')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeline_ads', to='common.ad', verbose_name='ad')),
            ],
            options={
                'verbose_name': 'Timeline ad',
                'verbose_name_plural': 'Timeline ads',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SingleAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='single_ads', to='common.ad', verbose_name='ad')),
            ],
            options={
                'verbose_name': 'Single ad',
                'verbose_name_plural': 'Single ads',
            },
        ),
        migrations.CreateModel(
            name='MainAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('ad1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_ad1', to='common.ad', verbose_name='ad1')),
                ('ad2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_ad2', to='common.ad', verbose_name='ad2')),
                ('ad3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='main_ad3', to='common.ad', verbose_name='ad3')),
            ],
            options={
                'verbose_name': 'Main ad',
                'verbose_name_plural': 'Main ads',
            },
        ),
        migrations.CreateModel(
            name='ContactItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('type', models.CharField(choices=[('phone', 'phone'), ('email', 'email'), ('telegram', 'telegram'), ('link', 'link')], max_length=25, verbose_name='type')),
                ('link', models.URLField(blank=True, null=True, verbose_name='link')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('telegram_link', models.URLField(blank=True, null=True, verbose_name='telegram link')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region='UZ', verbose_name='phone number')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='common.contact', verbose_name='contact')),
            ],
            options={
                'verbose_name': 'Contact item',
                'verbose_name_plural': 'Contact items',
            },
        ),
        migrations.CreateModel(
            name='BaseAd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated date')),
                ('ad1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_ad1', to='common.ad', verbose_name='ad1')),
                ('ad2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='base_ad2', to='common.ad', verbose_name='ad2')),
            ],
            options={
                'verbose_name': 'Base ad',
                'verbose_name_plural': 'Base ads',
            },
        ),
    ]