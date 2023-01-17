# Generated by Django 3.1.3 on 2023-01-17 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('router', '0006_auto_20230118_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='route',
            name='bench',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='route',
            name='key',
            field=models.TextField(default='jPB1jhu', help_text='Use generated short link or add any random characters of your choice to shorten it.', unique=True),
        ),
    ]