from rest_framework import serializers
from crawldata.models import UserMail , TimeSend

class UserMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMail
        fields = ('id','user_mail')

class TimeSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSend
        fields = ('id','user','hour','minute')

