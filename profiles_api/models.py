from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserProfileManager(BaseUserManager):
	"""manager for user Profiles"""

	def  create_user(self, email, name, password=None):
		"""Create a new user profile"""
		if not email:
			raise ValueError('Usre must have a amail address')

		email = self.normailize_email(email)
		user = self.model(email=email, name=name)

		user.set_password(password)
		user.save(using=self._db)

		return user


	def  create_superuser(self, email, name, password):
		"""Create a new superuser profile"""
		user = self.create_user(email, name, password)

		user.is_superuser = True
		user.is_staff = True
		user.save(using=self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""For users in System"""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = ['name']

	def get_full_name(self):
		"""Retrieve full name of User"""
		return self.name

	def get_short_name(self):
		"""Retrieve full name"""
		return self.name

	def __str__(self):
		"""string representation of user"""
		return self.email

