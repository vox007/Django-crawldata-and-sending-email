# Generated by Django 3.0.4 on 2020-03-23 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('link', models.TextField()),
                ('img_src', models.TextField()),
                ('time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='UserMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_mail', models.EmailField(max_length=254)),
                ('auto_send_mail', models.BooleanField(default=False)),
            ],
        ),
    ]
