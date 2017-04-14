from django.contrib import admin

from models import Room


class RoomAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('id', 'name', 'room_id')
	search_fields = ('id',)

admin.site.register(Room, RoomAdmin)
