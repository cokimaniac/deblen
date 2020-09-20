"""Debtor urls"""

from django.urls import path

#views
from debtors import views

urlpatterns = [
	path(
		route="",
		name="debtor",
		view=views.DebtorView.as_view()
	)
]