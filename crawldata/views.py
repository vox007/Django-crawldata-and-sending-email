from django.shortcuts import render, redirect, get_object_or_404
from .models import UserMail, TimeSend
from . import forms


def add_user(request):
    sub = forms.Subcribe()
    old_user = UserMail.objects.all()
    context = {
        'old_user': old_user,
    }
    if request.method == "POST":
        if sub.is_valid:
            new_user = UserMail()
            new_user.user_mail = request.POST['email']
            new_user.auto_send_mail = True
            new_user.save()
        return render(request, 'index/subscribe.html', context)
    return render(request, 'index/subscribe.html', context)


def remove_user(request, id):
    user = get_object_or_404(UserMail, id=id)
    if request.method == "POST":
        user.delete()
    return redirect('/')


def choose_time(request, id):
    time_choose = forms.TimeForm()
    if request.method == "POST":
        user = get_object_or_404(UserMail, id=id)
        user.auto_send_mail = False
        user.save()
        if time_choose.is_valid:
            time_send = TimeSend()
            time_send.user = get_object_or_404(UserMail, id=id)
            time_send.hour = request.POST['hour']
            time_send.minute = request.POST['minute']
            time_send.save()
    return redirect('/')
