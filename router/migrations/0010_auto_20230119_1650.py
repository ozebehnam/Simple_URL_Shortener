# Generated by Django 3.1.3 on 2023-01-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0009_auto_20230119_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='key',
            field=models.TextField(default='DyVc5Y4', help_text='Use generated short link or add any random characters of your choice to shorten it.', unique=True),
        ),
    ]
