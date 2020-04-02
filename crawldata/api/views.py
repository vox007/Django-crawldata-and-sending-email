from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from django.shortcuts import get_object_or_404

from crawldata.models import UserMail,TimeSend

from . serializers import UserMailSerializer,TimeSendSerializer

class UserListAPIView(ListCreateAPIView):
    queryset = UserMail.objects.all()
    serializer_class = UserMailSerializer

class UserDetailAPIView(RetrieveDestroyAPIView):
    queryset = UserMail.objects.all()
    serializer_class = UserMailSerializer

class TimeSendListAPIView(ListCreateAPIView):
    queryset = TimeSend.objects.all()
    serializer_class = TimeSendSerializer

class TimeSendDetailDeleteAPIView(RetrieveDestroyAPIView):
    queryset = TimeSend.objects.all()
    serializer_class = TimeSendSerializer