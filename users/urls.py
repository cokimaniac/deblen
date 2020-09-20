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
		route="signin",
		name="signin",
		view=views.signupAccount
	)
]

router = SimpleRouter()
router.register("", views.AccountViewSet)
urlpatterns += router.urls