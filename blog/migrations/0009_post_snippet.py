# Generated by Django 3.0.3 on 2021-06-10 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20210610_1618'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click title to read the post...', max_length=255),
        ),
    ]