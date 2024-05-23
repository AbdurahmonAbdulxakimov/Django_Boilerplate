# Generated by Django 4.2.2 on 2023-07-13 07:52

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'AuthorRecommendList user with that username already exists.'},
                                   help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                   max_length=150, null=True,
                                   validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                                   verbose_name='username'),
        ),
    ]
