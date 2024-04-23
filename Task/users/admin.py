from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = [
        "username",
        "email",
        "experience",
        "first_name",
        "last_name",
        "role",
    ]
    list_filter = ["username", "email"]
    search_fields = ["username"]
    list_editable = ["role"]
