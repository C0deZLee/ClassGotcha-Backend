from models import Moment, Post, Comment, Note, Rate

from django.contrib import admin


class MomentAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('creator', 'created', 'flagged', 'deleted')

	list_filter = ['created']

	fieldsets = (
		('Content', {'fields': ('pk', 'content', 'images',)}),
		('Info', {'fields': ('creator', 'classroom',)}),
		('Info', {'fields': ('deleted', 'solved', 'flagged')}),
		('Timestamp', {'fields': ('created',)}),
	)
	readonly_fields = ('created', 'creator', 'classroom', 'flagged', 'pk')


class PostAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('title', 'created', 'creator', 'flagged')

	list_filter = ['created']


class CommentAdmin(admin.ModelAdmin):
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.
	list_display = ('created', 'creator')

	list_filter = ['created']


class NoteAdmin(admin.ModelAdmin):
	list_display = ('title', 'creator', 'classroom')

	fieldsets = (
		('', {'fields': ('title', 'description', 'file',)}),
		('Info', {'fields': ('creator', 'classroom', 'tags')}),
		('Timestamp', {'fields': ('created',)}),
	)

	readonly_fields = ('created', 'creator', 'classroom')


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


class RateAdmin(admin.ModelAdmin):
	list_display = ('creator', 'num', 'note')


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


admin.site.register(Moment, MomentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Rate, RateAdmin)
