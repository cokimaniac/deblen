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
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

#serializers
from users.serializers import AccountSerializer, SignupAccountSerializer

#models
from users.models import Account

class AccountViewSet(ModelViewSet):
	"""
	Account View Set
	"""
	permission_classes = [IsAuthenticated,]
	serializer_class = AccountSerializer
	queryset = Account.objects.all()
	lookup_field = 'username'
	http_method_names = ["get", "patch"]

	def partial_update(self, request, *args, **kwargs):
		username = self.get_object().username
		if username == request.user.username:
			kwargs["partial"] = True
			return self.update(request, *args, **kwargs)
		return Response({"error": "Unauthorized action!"}, status=status.HTTP_403_FORBIDDEN)

@api_view(["POST"])
def signupAccount(request):
	"""
	Signup account view.
	"""
	serializer = SignupAccountSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
		return Response({
			"message": "Signup successful!"
		})

class LoginView(APIView):
	"""
	User account login view.
	"""
	def post(self, request):
		email = request.data.get("email")
		password = request.data.get("password")

		user = authenticate(email=email, password=password)

		if not user:
			return Reponse({
				"error": "Login Failed"
			}, status=status.HTTP_401_UNAUTHORIZED)
		token, _ = Token.objects.get_or_create(user=user)
		return Response({"token": token.key})