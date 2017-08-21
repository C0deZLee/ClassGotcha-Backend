from django.contrib import admin

from models import Badge, BadgeType


class BadgeAdmin(admin.ModelAdmin):
	list_display = ('id', 'badge_type', 'account', 'started')
	fieldsets = (
		('Basic', {'fields': ('id', 'badge_type', 'account')}),
		('Process', {'fields': ('started', 'finished')})
	)
	readonly_fields = ('started', 'id')


class BadgeTypeAdmin(admin.ModelAdmin):
	list_display = ('id', 'name',)

admin.site.register(Badge, BadgeAdmin)
admin.site.register(BadgeType, BadgeTypeAdmin)
