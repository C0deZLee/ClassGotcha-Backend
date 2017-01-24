from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class Avatar(models.Model):
	avatar4x = models.ImageField(upload_to='avatars', null=True, blank=True)
	avatar2x = models.ImageField(upload_to='avatars', null=True, blank=True)
	avatar1x = models.ImageField(upload_to='avatars', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)


class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		"""
		Creates and saves a User with the given email, username and password.
		"""
		if not email:
			raise ValueError('Users must have a valid email address')

		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username')

		account = self.model(email=self.normalize_email(email), username=kwargs.get('username'))

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)

		account.is_staff = True
		account.is_superuser = True
		account.save()

		return account


class Account(AbstractBaseUser, PermissionsMixin):
	# Basic
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	# Rule
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_student = models.BooleanField(default=True)
	is_professor = models.BooleanField(default=False)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	# Personal info
	first_name = models.CharField(max_length=40, blank=True)
	mid_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	gender = models.CharField(max_length=40, blank=True)
	birthday = models.DateField(null=True, blank=True)
	school_year = models.CharField(max_length=40, blank=True)
	avatar = models.ForeignKey(Avatar, blank=True, null=True, related_name='user_profiles_avatars')
	# Relations
	friends = models.ManyToManyField("self")
	major = models.ForeignKey('classrooms.Major', blank=True, null=True)
	# Relatives
	# 1) teaches
	# 2) classrooms
	# 3) comments
	# 4) joined_groups
	# 5) created_groups
	# 6) notes
	# 7) posts
	# 8) moments
	# 9) tasks
	# 10) rooms
	# Manager
	objects = AccountManager()
	# Settings
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	class Meta:
		ordering = ['created']

	def __unicode__(self):
		return self.username

	@property
	def get_full_name(self):
		"""Returns the person's full name."""
		return '%s %s' % (self.first_name, self.last_name)

	def get_short_name(self):
		return self.first_name

	def add_friends(self, value):
		pass

	def post_moments(self, value):
		pass

	@property
	def is_admin(self):
		return self.is_staff
