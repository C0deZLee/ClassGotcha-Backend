from django.contrib import admin

from models import Task


class TaskAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('pk', 'task_name', 'type', 'classroom')
	# list_filter = ('is_admin', 'school_year')
	# fieldsets = (
	#     (None, {'fields': ('email', 'username', 'password')}),
	#     ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'school_year', 'major', 'avatar')}),
	#     ('Permissions', {'fields': ('is_admin', 'is_student', 'is_professor')}),
	# )
	# readonly_fields = ('created', 'updated')
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

	# Fix admin saving issue
	# all classroom students and group members to the involved section
	def save_related(self, request, form, formsets, change):
		super(TaskAdmin, self).save_related(request, form, formsets, change)
		# only apply this when first created
		if not form.instance.involved:
			if form.instance.classroom:
				for student in form.instance.classroom.students.all():
					form.instance.involved.add(student)
				form.instance.save()
			elif form.instance.group:
				for member in form.instance.group.members.all():
					form.instance.involved.add(member)
				form.instance.save()


admin.site.register(Task, TaskAdmin)
