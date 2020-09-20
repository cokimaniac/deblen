"""
Debtor views.
"""

#drf
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

#models
from users.models import Account
from debtors.models import Debtor

#serializers
from debtors.serializers import DebtorSerializer

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