from models import Notification
from django.contrib import admin


class NotificationAdmin(admin.ModelAdmin):
	pass


admin.site.register(Notification, NotificationAdmin)