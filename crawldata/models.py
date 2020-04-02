from django.db import models
from django.db.models.signals import pre_save, pre_delete
from django.core.exceptions import ObjectDoesNotExist
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json


class Article(models.Model):
    title = models.CharField(max_length=40)
    link = models.TextField()
    img_src = models.TextField()
    time = models.DateTimeField()

    def __str__(self):
        return self.title


class UserMail(models.Model):
    user_mail = models.EmailField()
    auto_send_mail = models.BooleanField(default=False)

    def __str__(self):
        return self.user_mail

class TimeSend(models.Model):
    user = models.ForeignKey(UserMail,on_delete=models.CASCADE)
    hour = models.CharField(max_length=10, blank=True, null=True)
    minute = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.user_mail

    def get_or_create_crontab(self):
        schedule, created = CrontabSchedule.objects.get_or_create(
            minute=self.minute,
            hour=self.hour,
            day_of_week='*',
            day_of_month='*',
            timezone='Asia/Bangkok',
        )
        return schedule

    def set_periodic_task(self, task_name):
        schedule = self.get_or_create_crontab()
        PeriodicTask.objects.create(
            crontab=schedule,
            name=f'{self.user.user_mail}-{self.user.id}',
            task=task_name,
            kwargs=json.dumps({
                'recepient': self.user.user_mail,
            })
        )

    def get_periodic_task(self, task_name):
        periodic_task = PeriodicTask.objects.get(
            name=f'{self.user.user_mail}-{self.user.id}',
            task=task_name,
        )
        return periodic_task

    def update_periodic_task(self, task_name):
        periodic_task = self.get_periodic_task(task_name)
        periodic_task.delete()
        self.set_periodic_task(task_name)


@receiver(pre_save, sender=TimeSend)
def set_or_update_periodic_task(sender, instance=None, created=True, **kwargs):
    if created:
        try:
            instance.update_periodic_task(task_name='crawldata.tasks.sending_email')
        except ObjectDoesNotExist:
            instance.set_periodic_task(task_name='crawldata.tasks.sending_email')
