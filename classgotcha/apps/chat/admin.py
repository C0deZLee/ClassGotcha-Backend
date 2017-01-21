from django.contrib import admin

from models import Room, Message


class RoomAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('id', 'name', 'created')


class MessageAdmin(admin.ModelAdmin):
	list_display = ('id', 'room', 'created')

	fieldsets = (
		('Info', {'fields': ('room', 'username')}),
		('Content', {'fields': ('message',)}),
		('Timestamp', {'fields': ('created',)})
	)
	readonly_fields = ('created',)


admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
