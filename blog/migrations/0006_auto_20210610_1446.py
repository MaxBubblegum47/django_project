# Generated by Django 3.0.3 on 2021-06-10 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20210610_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['date_posted']},
        ),
    ]
