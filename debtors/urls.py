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
	path(
		route="<int:id>/ammounts/",
		name="ammount",
<<<<<<< HEAD
		view=views.AmmountView.as_view()
=======
		view=views.DebtorAmmountView.as_view()
>>>>>>> a5a23cd2e0a6d781476588b4303fb2b41861b6b4
	)
]