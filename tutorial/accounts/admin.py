from django.contrib import admin
from django.contrib import auth
from accounts.models import UserProfile

# Register your models here.
admin.site.register(UserProfile)
