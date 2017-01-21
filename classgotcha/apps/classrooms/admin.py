from django.contrib import admin

from models import Classroom, Semester, Major
from ..chat.models import Room, Account


class ClassroomAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('class_code', 'class_name', 'major', 'class_number',
	                'class_section', 'class_credit', 'students_count')
	list_filter = ('major',)

	fieldsets = (
		('Class Info', {'fields': ('class_code', 'class_name', 'major', 'class_number', 'class_credit')}),
		('Descr', {'fields': ('description', 'syllabus')}),
		('Time', {'fields': ('semester', 'start', 'end', 'repeat', 'class_room')}),
		('Enrolled', {'fields': ('professor', 'students', 'chatroom')}),
		('Timestamp', {'fields': ('created', 'updated',)}),
	)
	readonly_fields = ('created', 'updated',)

	# # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# # overrides get_fieldsets to use this attribute when creating a user.
	# add_fieldsets = (
	#     (None, {
	#         'classes': ('wide',),
	#         'fields': ('email', 'username', 'password1', 'password2')}
	#      ),
	# )
	# search_fields = ('email', 'username')
	# ordering = ('email',)
	# filter_horizontal = ()

	def save_related(self, request, form, formsets, change):
		super(ClassroomAdmin, self).save_related(
			request, form, formsets, change)

		# only apply this when first created, when classroom first created, no
		# chatroom pk
		if not form.instance.chatroom:
			# TODO: UNSTABLE! Only retrieve the first admin user as the class
			# chat room controller
			room = Room.objects.create(creator=Account.objects.get(username='admin'))
			room.name = form.instance.major.major_short + ' ' + \
			            form.instance.class_number + ' - ' + form.instance.class_section + ' Chat Room'
			room.save()
			form.instance.chatroom = room
			form.instance.save()


class SemesterAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'start', 'end')


class MajorAdmin(admin.ModelAdmin):
	list_display = ('major_short', 'major_full', 'major_college')
	list_filter = ['major_college']


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Major, MajorAdmin)
