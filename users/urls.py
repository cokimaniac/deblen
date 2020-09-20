"""
Users urls.
"""

#django
from django.urls import path

#drf
from rest_framework.routers import SimpleRouter

#views
from users import views

urlpatterns = [
	path(
		route="signup",
		name="signup",
		view=views.signupAccount
	),
	path(
		route="login",
		name="login",
		view=views.LoginView.as_view()
	),
]

router = SimpleRouter()
router.register("", views.AccountViewSet)
urlpatterns += router.urls