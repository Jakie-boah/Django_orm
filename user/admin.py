from django.contrib import admin
from user.models import UserProfile, User
from django.contrib.auth.admin import UserAdmin

fields = list(UserAdmin.fieldsets)
fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'age', 'nickname')})

UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
