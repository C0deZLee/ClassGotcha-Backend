from rest_framework import permissions


class IsAdminOrSelf(permissions.BasePermission):
	def has_permission(self, request, view):
		# allow user to list all users if logged in user is staff
		return request.user

	def has_object_permission(self, request, view, obj):
		# allow logged in user to view own details, allows staff to view all records
		return request.user.is_staff or obj == request.user


class AllowAny(permissions.BasePermission):
	def has_permission(self, request, view):
		# allow anyone to list all users
		return True

	def has_object_permission(self, request, view, obj):
		# allow anyone to view anyone's details
		return True

class IsAnonymous(permissions.BasePermission):
	def has_permission(self, request, view):
		return not request.user
	def has_object_permission(self, request, view, obj):
		return not request.user