# Generated by Django 4.2.2 on 2023-07-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0016_ad_title_en_us_contact_title_en_us_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='title_en_us',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='title_en_us',
            new_name='title_en',
        ),
        migrations.RenameField(
            model_name='staticpage',
            old_name='content_en_us',
            new_name='content_en',
        ),
        migrations.RemoveField(
            model_name='staticpage',
            name='title_en_us',
        ),
        migrations.AddField(
            model_name='staticpage',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='staticpage',
            name='slug_from_lang',
            field=models.CharField(blank=True, choices=[('uz', 'Uzbek'), ('ru', 'Russian'), ('en', 'English')], max_length=64, null=True, verbose_name='select the language of the slug'),
        ),
    ]