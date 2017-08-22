from django.contrib import admin
from django.core.urlresolvers import reverse

from models import Task
from ..classrooms.models import Classroom


class InlineEditLinkMixin(object):
	readonly_fields = ['edit_details']
	edit_label = "EDIT"

	def edit_details(self, obj):
		if obj.id:
			opts = self.model._meta
			return "<a href='%s' target='_blank'>%s</a>" % (reverse(
				'admin:%s_%s_change' % (opts.app_label, opts.object_name.lower()),
				args=[obj.id]
			), self.edit_label)
		else:
			return "(save to edit details)"

	edit_details.allow_tags = True


class ClassroomInline(InlineEditLinkMixin, admin.TabularInline):
	model = Classroom
	extra = 0
	fields = ('class_name', 'class_code', 'edit_details')
	readonly_fields = ('class_name', 'class_code', 'edit_details')


class TaskAdmin(admin.ModelAdmin):
	list_display = ('pk', 'task_name', 'type', 'category')

	list_filter = ('type', 'category')

	search_fields = ('task_name', 'type', 'category')
	fieldsets = (
		('Task Info', {'fields': ('task_name', 'description', 'location', 'category', 'type')}),
		('Time', {'fields': ('start', 'end',)}),
		('Repeat', {'fields': ('repeat', 'repeat_start', 'repeat_end')}),
		('Involved', {'fields': ('involved', 'group')}),
	)

	inlines = [ClassroomInline]

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
