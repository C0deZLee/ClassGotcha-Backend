from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group as AdminGroup

from forms import UserChangeForm, UserCreationForm
from models import Account, Group, Professor, AccountVerifyToken


class AccountAdmin(UserAdmin):
	# The forms to add and change user instances
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ('id', 'email', 'username', 'get_full_name', 'school_year', 'is_staff', 'is_verified')
	list_filter = ['is_staff', 'school_year']
	fieldsets = (
		(None, {'fields': ('email', 'username', 'password', 'matrix_token')}),
		('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'school_year', 'major', 'avatar1x', 'avatar2x')}),
		('Permissions', {'fields': ('is_professor', 'is_verified', 'is_staff', 'is_superuser')}),
		('Timestamp', {'fields': ('created', 'updated')})
	)
	readonly_fields = ('created', 'matrix_token', 'updated', 'is_staff', 'is_superuser', 'is_professor')
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')}
		 ),
	)
	search_fields = ('email', 'username')
	ordering = ('email',)


class GroupAdmin(admin.ModelAdmin):
	list_display = ('group_type', 'creator', 'classroom')
	list_filter = ['group_type']

	def get_members(self):
		return "\n".join([a.username for a in self.members.all()])


class ProfessorAdmin(admin.ModelAdmin):
	list_display = ('first_name', 'last_name', 'department', 'major')
	fieldsets = (
		(None, {'fields': ('email', 'first_name', 'last_name')}),
		('major', {'fields': ('department', 'major', 'office')}),
		# ('Permissions', {'fields': ('is_professor', 'is_staff', 'is_superuser')}),
		('Timestamp', {'fields': ('created',)})
	)
	search_fields = ('first_name', 'last_name')
	readonly_fields = ('department', 'created')


class AccountVerifyTokenAdmin(admin.ModelAdmin):
	list_display = ('account', 'is_expired')
	fieldsets = (
		(None, {'fields': ('account', 'token', 'expire_time', 'is_expired')}),
	)
	readonly_fields = ('is_expired', 'expire_time')


admin.site.register(Group, GroupAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(AccountVerifyToken, AccountVerifyTokenAdmin)
admin.site.unregister(AdminGroup)
