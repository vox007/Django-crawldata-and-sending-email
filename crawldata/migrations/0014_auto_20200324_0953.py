# Generated by Django 3.0.4 on 2020-03-24 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawldata', '0013_auto_20200324_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermail2',
            name='hour',
            field=models.IntegerField(default=1),
        ),
    ]
