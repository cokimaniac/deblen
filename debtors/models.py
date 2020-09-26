"""
Debtor models.
"""

from django.db import models
from users.models import Account

class Debtor(models.Model):
	"""
	Debtor model.
	User account debtors.
	"""
	account = models.ForeignKey(Account, on_delete=models.CASCADE)
	phone_number = models.CharField(
		verbose_name="Debtor phone number",
		max_length=40,
		blank=False
	)
	full_name = models.CharField(
		verbose_name="Debtor full name",
		max_length=80,
		blank=False
	)
	email = models.EmailField(
		verbose_name="Debtor email",
		max_length=60
	)

	REQUIRED_FIELDS = ["full_name", "phone_number"]

	def __str__(self):
		return self.full_name

class Ammount(models.Model):
	"""
	Debtor ammount of money that ows to lender.
	"""
	debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
	money = models.IntegerField(
		verbose_name="Debtor ammount",
		blank=False
	)
	loan_date = models.DateTimeField(
		verbose_name="Date loan ammount",
		auto_now_add=True
	)
	loan_payment_date = models.DateTimeField(
		verbose_name="Date loan date payment",
	)

	def __str__(self):
		return self.debtor.full_name
