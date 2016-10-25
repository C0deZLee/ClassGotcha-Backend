from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class Major(models.Model):
	major_short = models.CharField(max_length=10)
	major_full = models.CharField(max_length=100)
	major_college = models.CharField(max_length=100)


class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		"""
		Creates and saves a User with the given email, username and password.
		"""
		if not email:
			raise ValueError('Users must have a valid email address')

		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username')

		account = self.model(
				email=self.normalize_email(email), username=kwargs.get('username')
		)

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)

		account.is_admin = True
		account.is_superuser = True
		account.save()

		return account


class Account(AbstractBaseUser, PermissionsMixin):
	# Basic
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	# Rule
	is_admin = models.BooleanField(default=False)
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
	avatar = models.URLField(blank=True)
	# models.ImageField(
	#     upload_to="public/uploads/avatars/",
	#     height_field="qr_image_height",
	#     width_field="qr_image_width",
	#     null=True,
	#     blank=True,
	#     editable=False
	# )
	# Relations
	friends = models.ManyToManyField("self")
	major = models.ForeignKey(Major, blank=True, null=True)
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
	def is_staff(self):
		return True
