from django.contrib import admin

from models import Classroom, Semester
from ..chat.models import Room
from ..accounts.models import Account


class ClassroomAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('class_code', 'major', 'class_number', 'class_name', 'section', 'students_count')
	list_filter = ('major',)
	# fieldsets = (
	#     (None, {'fields': ('email', 'username', 'password')}),
	#     ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'school_year', 'major', 'avatar')}),
	#     ('Permissions', {'fields': ('is_admin', 'is_student', 'is_professor')}),
	# )
	readonly_fields = ('updated',)

	# # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# # overrides get_fieldsets to use this attribute when creating a user.
	# add_fieldsets = (
	#     (None, {
	#         'chatroom': ('class_chatroom',)
	#     }
	#      ),
	# )
	# search_fields = ('email', 'username')
	# ordering = ('email',)
	# filter_horizontal = ()

	def save_related(self, request, form, formsets, change):
		super(ClassroomAdmin, self).save_related(request, form, formsets, change)

		# only apply this when first created
		if not form.instance.chatroom:
			room = Room.objects.create(creator = Account.objects.get(pk=1))
			room.name = form.instance.major.major_short + ' ' + form.instance.class_number + ' - ' + form.instance.class_section +' Chat Room'
			# TODO: UNSTABLE! Only retrieve the first admin user as the class chat room controller
			room.save()
			form.instance.chatroom = room


class SemesterAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'start', 'end')


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Semester, SemesterAdmin)
