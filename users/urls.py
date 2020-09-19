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
        route="",
        name="users",
        view=views.AccountView.as_view()
    )
]