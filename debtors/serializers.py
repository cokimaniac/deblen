"""
Debtor serializers.
"""

from rest_framework import serializers

#models
from debtors.models import Debtor

class DebtorSerializer(serializers.ModelSerializer):
	"""
	Debtor model serializer.
	"""
	class Meta:
		fields = ["account", "phone_number", "full_name"]
		model = Debtor

	def create(self, validate_data):
		password = validate_data.pop("password")
		debtor = Debtor.objects.create(**validate_data)
		debtor.save()
		return debtor