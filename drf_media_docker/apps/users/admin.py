from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('info',)
    fieldsets = UserAdmin.fieldsets + (
        ('info', {
            'fields': ('info',)
        }),
    )
