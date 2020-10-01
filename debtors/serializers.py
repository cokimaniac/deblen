"""
Debtor serializers.
"""

from rest_framework import serializers

#models
from debtors.models import Debtor, Ammount

class DebtorSerializer(serializers.ModelSerializer):
	"""
	Debtor model serializer.
	"""
	class Meta:
		fields = ["id", "account", "phone_number", "full_name"]
		model = Debtor

	def create(self, validate_data):
		password = validate_data.pop("password")
		debtor = Debtor.objects.create(**validate_data)
		debtor.save()
		return debtor

class AmmountSerializer(serializers.ModelSerializer):
	"""
	Ammount of debtor serializer.
	"""
	class Meta:
		fields = ["money", "loan_payment_date"]
		model = Ammount