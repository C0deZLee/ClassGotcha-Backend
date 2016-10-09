from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


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
	first_name = models.CharField(max_length=40)
	mid_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)

	gender = models.CharField(max_length=40)
	birthday = models.DateField(null=True)
	school_year = models.CharField(max_length=40)
	major = models.CharField(max_length=40)
	avatar = models.URLField()
	# models.ImageField(
	#     upload_to="public/uploads/",
	#     height_field="qr_image_height",
	#     width_field="qr_image_width",
	#     null=True,
	#     blank=True,
	#     editable=False
	# )
	# Relations
	friends = models.ManyToManyField("self")
	# Manager
	objects = AccountManager()
	# Settings
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __unicode__(self):
		return self.username

	@property
	def get_full_name(self):
		"Returns the person's full name."
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
