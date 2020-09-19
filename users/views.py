"""
Users views.
"""

from django.shortcuts import render

#drf
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

#serializers
from users.serializers import AccountSerializer, SignupAccountSerializer

#models
from users.models import Account

class AccountView(APIView):
	def get(self, request):
		accounts = Account.objects.all()
		serialized_accounts = AccountSerializer(accounts, many=True)
		return Response(serialized_accounts.data)

	def post(self, request):
		serializer = SignupAccountSerializer(data=request.data)
		if serializer.is_valid():
			account = serializer.save()
			return Response({
				"message": "Great! User account created succesfully"
			})
		return Response({
			"errors": serializer.errors
		})