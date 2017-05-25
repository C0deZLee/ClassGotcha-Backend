from django.contrib import admin

from models import Chatroom


class ChatroomAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('id', 'room_name')
	search_fields = ('id',)

admin.site.register(Chatroom, ChatroomAdmin)
