# Generated by Django 3.0.4 on 2020-03-24 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crawldata', '0010_usermail2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermail2',
            name='minute',
        ),
    ]
