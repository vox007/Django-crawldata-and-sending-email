from django import forms
from . models import TimeSend

class TimeForm(forms.Form):
    # crete a class Meta
    class Meta:
        model = TimeSend
        fields = ["hour", "minute"]


class Subcribe(forms.Form):
    email = forms.EmailField()

    def __str__(self):
        return self.email
