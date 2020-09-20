"""
Users views.
"""

#django
from django.shortcuts import render
from django.contrib.auth import authenticate

#drf
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

#serializers
from users.serializers import AccountSerializer, SignupAccountSerializer

#models
from users.models import Account

class AccountViewSet(ModelViewSet):
	permission_classes = [IsAuthenticated,]
	serializer_class = AccountSerializer
	queryset = Account.objects.all()
	lookup_field = 'username'

	def create(self, request, *args, **kwargs):
		return Response({"error": "Method POST is not allowed!"}, status=HTTP_401_UNAUTHORIZED)

@api_view(["POST"])
def signupAccount(request):
	serializer = SignupAccountSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({
			"message": "Signup successful!"
		})

class LoginView(APIView):
	"""
	User lovin view.
	"""
	def post(self, request):
		email = request.data.get("email")
		password = request.data.get("password")

		user = authenticate(email=email, password=password)

		if not user:
			return Reponse({
				"error": "Login Failed"
			}, status=HTTP_401_UNAUTHORIZED)
		token, _ = Token.objects.get_or_create(user=user)
		return Response({"token": token.key})