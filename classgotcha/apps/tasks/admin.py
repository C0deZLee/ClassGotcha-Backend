from django.contrib import admin

from models import Task


class TaskAdmin(admin.ModelAdmin):
	list_display = ('pk', 'task_name', 'type', 'classroom')

	list_filter = ('type',)

	fieldsets = (
		('Task Info', {'fields': ('task_name', 'description', 'location')}),
		('Time', {'fields': ('start', 'end', 'due')}),
		('Repeat', {'fields': ('repeat', 'repeat_start', 'repeat_end')}),
		('Involved', {'fields': ('involved', 'classroom', 'group')}),
	)
	readonly_fields = ('involved', 'classroom', 'group')

	# Fix admin saving issue
	# all classroom students and group members to the involved section
	def save_related(self, request, form, formsets, change):
		super(TaskAdmin, self).save_related(request, form, formsets, change)
		# only apply this when first created (no involved when first created)
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
