from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from forms import UserChangeForm, UserCreationForm
from models import Account, Avatar


class AccountAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id', 'email', 'username', 'get_full_name', 'school_year', 'is_staff')
    list_filter = ['is_staff', 'school_year']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'gender', 'school_year', 'major', 'avatar')}),
        ('Permissions', {'fields': ('is_student', 'is_professor', 'is_staff', 'is_superuser')}),
        ('Timestamp', {'fields': ('created', 'updated')})
    )
    readonly_fields = ('created', 'updated', 'is_staff', 'is_superuser')
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    #
    # def classrooms(self):


class AvatarAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_image')

# Now register the new UserAdmin...
admin.site.register(Account, AccountAdmin)
admin.site.register(Avatar, AvatarAdmin)
# ... and, since we're not using Django's built-in permissions, unregister the Group model from admin.
admin.site.unregister(Group)
