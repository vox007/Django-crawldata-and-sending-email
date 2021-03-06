# Generated by Django 3.0.4 on 2020-04-02 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawldata', '0024_remove_usermail_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermail',
            name='hour',
        ),
        migrations.RemoveField(
            model_name='usermail',
            name='minute',
        ),
        migrations.AddField(
            model_name='usermail',
            name='auto_send_mail',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='TimeSend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hour', models.CharField(blank=True, max_length=10, null=True)),
                ('minute', models.CharField(blank=True, max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crawldata.UserMail')),
            ],
        ),
    ]
