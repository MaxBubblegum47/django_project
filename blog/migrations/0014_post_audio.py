# Generated by Django 3.2.6 on 2021-08-02 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_rename_approved_comment_report_approved_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='audio',
            field=models.FileField(default='cash.mp3', upload_to=''),
        ),
    ]
