from models import Notification
from django.contrib import admin


class NotificationAdmin(admin.ModelAdmin):
	list_display = ['sender', 'receiver', 'read', 'created']


admin.site.register(Notification, NotificationAdmin)
