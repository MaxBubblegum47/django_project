# Generated by Django 3.0.3 on 2021-06-11 00:07

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Bio', verbose_name=django.contrib.auth.models.User),
        ),
    ]
