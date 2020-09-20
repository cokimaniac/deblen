"""
Users models.
"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class AccountManager(BaseUserManager):
	def create_user(self, email, username, phone_number, password=None):
		if not email:
			raise ValueError("Users must be linked with a email")
		if not username:
			raise ValueError("Users must be linked with a username")
		if not phone_number:
			raise ValueError("Users must be linked with a phone number")

		user = self.model(
			email=self.normalize_email(email),
			username=username,
			phone_number=phone_number,
		)
		user.is_staff = True
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, phone_number, password):
		user = self.create_user(
			email=self.normalize_email(email),
			username=username,
			password=password,
			phone_number=phone_number
		)

		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

class Account(AbstractBaseUser):
	email = models.EmailField(
		verbose_name="Email",
		max_length=60,
		unique=True
	)
	username = models.CharField(
		verbose_name="Username",
		unique=True,
		max_length=30
	)
	date_joined = models.DateTimeField(
		verbose_name="Date Joined",
		auto_now_add=True
	)
	last_login = models.DateTimeField(
		verbose_name="Last Login",
		auto_now=True
	)
	is_admin = models.BooleanField(
		default=False
	)
	is_active = models.BooleanField(
		default=True
	)
	is_staff = models.BooleanField(
		default=False
	)
	is_superuser = models.BooleanField(
		default=False
	)

	first_name = models.CharField(
		verbose_name="First Name",
		max_length=70,
	)
	last_name = models.CharField(
		verbose_name="Last Name",
		max_length=70,
	)
	phone_number = models.CharField(
		verbose_name="Phone Number",
		max_length=20
	)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["username", "phone_number"]
	
	objects = AccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True