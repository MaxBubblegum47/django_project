# Generated by Django 3.0.3 on 2021-06-10 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_post_snippet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='snippet',
        ),
    ]
