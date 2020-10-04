"""
Users seriaizers.
"""

# drf
from rest_framework import serializers

# models
from users.models import Account


class AccountSerializer(serializers.ModelSerializer):
  """
  User serializer.
  """

  class Meta:
      model = Account
      fields = ["id", "username", "email", "first_name", "last_name", "phone_number"]


class SignupAccountSerializer(serializers.ModelSerializer):
  """
	User signup serializer.
	"""
  def create(self, validate_data):
      password = validate_data.pop("password")
      user = Account.objects.create(**validate_data)
      user.set_password(password)
      user.save()
      return user


  class Meta:
      model = Account
      fields = ["username", "email", "phone_number", "password"]
