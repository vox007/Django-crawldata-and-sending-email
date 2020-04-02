from django.urls import path
from . import views

app_name = "mail"

urlpatterns = [
    path('', views.add_user, name='add_user'),
    path('delete/<id>/', views.remove_user, name='delete_user'),
    path('choose/<id>/', views.choose_time, name='choose_time'),
]
