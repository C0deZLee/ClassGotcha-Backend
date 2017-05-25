from django.contrib import admin

from models import Classroom, Semester, Major
from ..chatrooms.models import Chatroom, Account


class ClassroomAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('class_code', 'class_name', 'major', 'class_number',
	                'class_section', 'class_credit', 'students_count')
	list_filter = ('major',)
	#
	fieldsets = (
		('Class Info', {'fields': ('class_code', 'class_name', 'major', 'class_number', 'class_credit', 'folders')}),
		('Descr', {'fields': ('description', 'syllabus')}),
		('Time', {'fields': ('semester', ('class_repeat', 'get_class_time'), 'class_time')}),
		('Enrolled', {'fields': ('professors', ('students', 'students_count'), )}),
		('Timestamp', {'fields': ('created', 'updated',)}),
	)
	readonly_fields = ('professors', 'major', 'created', 'updated', 'class_repeat', 'get_class_time', 'students_count', 'folders')

	# search_fields = ('class_code', 'id')

	def save_related(self, request, form, formsets, change):
		super(ClassroomAdmin, self).save_related(
			request, form, formsets, change)
		# only apply this when first created, when classroom first created, no
		# chatrooms pk
		if not form.instance.chatroom:
			# TODO: UNSTABLE! Only retrieve the first admin user as the class
			# chat room controller
			Room.objects.create(creator=Account.objects.get(is_staff=True),
			                    name=form.instance.major.major_short + ' ' + \
			                         form.instance.class_number + ' - ' + form.instance.class_section + ' Chat Room',
			                    classroom=form.instance)
			form.instance.task.classroom = form.instance
			form.instance.task.save()


class SemesterAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'start', 'end')


class MajorAdmin(admin.ModelAdmin):
	list_display = ('major_short', 'major_full', 'major_college')
	list_filter = ['major_college']


admin.site.register(Classroom, ClassroomAdmin)
admin.site.register(Semester, SemesterAdmin)
admin.site.register(Major, MajorAdmin)
