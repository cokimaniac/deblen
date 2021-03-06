"""
Debtor views.
"""

#python
from datetime import datetime
from moment import date

#drf
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

#models
from users.models import Account
from debtors.models import Debtor, Ammount

#serializers
from debtors.serializers import DebtorSerializer, AmmountSerializer

class DebtorView(APIView):
	"""
	Debtor view.
	"""
	permission_classes = [IsAuthenticated,]

	def get(self, request):
		debtors = Debtor.objects.all().filter(account=request.user)
		serializer = DebtorSerializer(debtors, many=True)
		return Response(serializer.data)

	def post(self, request):
		data = {
			"account": request.user.id,
			"full_name": request.data.get("full_name"),
			"phone_number": request.data.get("phone_number"),
		}
		serializer = DebtorSerializer(data=data)
		if serializer.is_valid():
			data = serializer.data
			account = Account.objects.get(username=request.user.username)
			debtor = Debtor(account=account)
			debtor.full_name = data.get("full_name")
			debtor.phone_number = data.get("phone_number")
			debtor.save()
			return Response(serializer.data)
		return Response({
			"error": serializer.errors
		})

class DebtorDetailView(RetrieveAPIView):
	"""
	Retrieve debtor view.
	"""
	serializer_class = DebtorSerializer
	queryset = Debtor.objects.all()
	permission_classes = [IsAuthenticated, ]
	http_method_names = ["get"]

class AmmountView(APIView):
	"""
	Debtor ammounts view.
	"""
	def get(self, request, id):
		ammount = Ammount.objects.all().filter(debtor=id)
		serializer = AmmountSerializer(ammount, many=True)
		return Response(serializer.data)

	def post(self, request, id):
		required_data = {
			"money": request.data.get("money"),
			"payment_months": request.data.get("payment_months"),
			"expected_payment_date": date(datetime.now()).add(months=int(request.data.get("payment_months"))).date,
		}
		serializer = AmmountSerializer(data=required_data)
		if serializer.is_valid():
			data = serializer.data
			debtor = Debtor.objects.get(id=id)
			ammount = Ammount(debtor=debtor)
			ammount.money = data.get("money")
			ammount.payment_months = data.get("payment_months")
			ammount.expected_payment_date = data.get("expected_payment_date")
			ammount.monthly_interest = data.get("money")*0.1
			ammount.save()
			return Response(serializer.data)
		return Response({"errors": serializer.errors})
