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