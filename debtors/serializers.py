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

	def create(self, validated_data):
		password = validated_data.pop("password")
		debtor = Debtor.objects.create(**validated_data)
		debtor.save()
		return debtor

class AmmountSerializer(serializers.ModelSerializer):
	"""
	Debtor ammount serializer.
	"""
	class Meta:
		fields = ["id", "money", "expected_payment_date", "payment_months", "payment_status", "debtor"]
		model = Ammount