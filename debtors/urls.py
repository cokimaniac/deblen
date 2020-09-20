"""Debtor urls"""

#django
from django.urls import path

#drf
from rest_framework.routers import SimpleRouter

#views
from debtors import views

urlpatterns = [
	path(
		route="<int:pk>/",
		name="detail",
		view=views.DebtorDetailView.as_view()
	),
	path(
		route="",
		name="debtor",
		view=views.DebtorView.as_view()
	),
]