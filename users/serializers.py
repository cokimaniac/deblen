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
        fields = ["username", "email", "first_name", "last_name", "phone_number"]


class SignupAccountSerializer(serializers.ModelSerializer):
    """
	User signup serializer.
	"""

    class Meta:
        model = Account
        fields = ["username", "email", "phone_number", "password"]
