# Generated by Django 3.0.4 on 2020-03-23 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawldata', '0008_auto_20200323_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermail',
            name='time_set',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]