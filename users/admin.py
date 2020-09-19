

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

#models
from users.models import Account

class UserDLAdmin(UserAdmin):
	list_display = ("email", "username", "first_name", "last_name", "date_joined", "last_login", "is_admin", "is_staff")
	search_fields = ("email", "username", "last_name", "first_name")
	readonly_fields = ("date_joined", "last_login")

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(Account, UserDLAdmin)