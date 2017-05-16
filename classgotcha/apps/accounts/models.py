from django.db import models
from django.db.models import Avg

from ..tags.models import Tag
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class Avatar(models.Model):
	avatar2x = models.ImageField(upload_to='avatars', null=True, blank=True)
	avatar1x = models.ImageField(upload_to='avatars', null=True, blank=True)
	created = models.DateTimeField(auto_now_add=True)


class AccountManager(BaseUserManager):
	def create_user(self, email, password=None, **kwargs):
		"""Creates and saves a User with the given email, username and password."""
		if not email:
			raise ValueError('Users must have a valid email address')

		if not kwargs.get('username'):
			raise ValueError('Users must have a valid username')

		account = self.model(email=self.normalize_email(email), username=kwargs.get('username'), )

		account.set_password(password)
		account.save()

		return account

	def create_superuser(self, email, password, **kwargs):
		account = self.create_user(email, password, **kwargs)

		account.is_staff = True
		account.is_superuser = True
		account.save()

		return account


# TODO: Some professors work for multiple departments,
# TODO: Some professors in same major has same name,
# TODO: same professors teach multiple majors' courses under same department
class Professor(models.Model):
	class Meta:
		unique_together = (('first_name', 'last_name', 'major'),)

	# Basic
	first_name = models.CharField(max_length=40)
	last_name = models.CharField(max_length=40)
	mid_name = models.CharField(max_length=40, blank=True)
	email = models.CharField(max_length=50)
	office = models.CharField(max_length=100, blank=True)
	# Relationship
	major = models.ForeignKey('classrooms.Major')
	tags = models.ManyToManyField(Tag)
	# Timestamp
	created = models.DateTimeField(auto_now_add=True)

	# Relationship
	# 1) comments
	# 2) rates
	# 3) classrooms
	# 4) office_hours

	def __unicode__(self):
		return '%s %s' % (self.first_name, self.last_name)

	@property
	def department(self):
		return self.major.department

	@property
	def full_name(self):
		return self.first_name + ' ' + self.last_name

	@property
	def avg_rate(self):
		return self.rates.all().aggregate(Avg('num'))


class Account(AbstractBaseUser, PermissionsMixin):
	# Basic
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)
	# Rule
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	# is_student = models.BooleanField(default=True)
	# is_professor = models.BooleanField(default=False)
	professor = models.ForeignKey(Professor, blank=True, null=True, related_name='account')
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
	about_me = models.CharField(max_length=200, default='Yo!')
	level = models.IntegerField(default=1)
	phone = models.CharField(max_length=20, null=True)
	matrix_token = models.CharField(max_length=200, null=True)
	# Relations
	friends = models.ManyToManyField('self')
	pending_friends = models.ManyToManyField('self')
	major = models.ForeignKey('classrooms.Major', blank=True, null=True)
	notifications = models.ManyToManyField('posts.Notification')
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
		return '%s %s' % (self.first_name, self.last_name)

	def get_short_name(self):
		return self.first_name

	@property
	def full_name(self):
		return '%s %s' % (self.first_name, self.last_name)

	def add_friends(self, value):
		pass

	def post_moments(self, value):
		pass

	@property
	def is_admin(self):
		return self.is_staff

	@property
	def is_professor(self):
		return self.professor_id is not None


class Group(models.Model):
	# Basic Info
	# class, subclass, individual, club
	group_type = models.CharField(max_length=20)
	# Relations
	members = models.ManyToManyField(Account, blank=True, related_name='joined_groups')
	classroom = models.ForeignKey('classrooms.Classroom', blank=True, null=True, related_name='groups')
	creator = models.ForeignKey(Account, related_name='created_groups')

# Relatives
# 1) chatroom
