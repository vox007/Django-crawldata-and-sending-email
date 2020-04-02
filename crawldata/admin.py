from django.contrib import admin

from . models import Article, UserMail, TimeSend

# Register field to the admin custom

admin.site.register(Article)
admin.site.register(UserMail)
admin.site.register(TimeSend)