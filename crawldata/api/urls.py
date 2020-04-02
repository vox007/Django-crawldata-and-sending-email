from django.urls import path
from . views import UserListAPIView,UserDetailAPIView,TimeSendListAPIView,TimeSendDetailDeleteAPIView

urlpatterns = [
    path('detail/',UserListAPIView.as_view(),name='user_list'),
    path('detail/<pk>/',UserDetailAPIView.as_view(),name='user_detail'),
    path('time',TimeSendListAPIView.as_view(),name='time_list'),
    path('time/<pk>',TimeSendDetailDeleteAPIView.as_view(),name='time_detail_delete'),
]