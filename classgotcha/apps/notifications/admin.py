from models import Notification
from django.contrib import admin


class NotificationAdmin(admin.ModelAdmin):
	list_display = ['send_from', 'receiver', 'read', 'created']


admin.site.register(Notification, NotificationAdmin)
