from django.contrib.auth.models import Group
from django.db import reset_queries, connection

from rest_framework.permissions import BasePermission


class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        """Returns True if the User is in the 'subscribers' Group"""

        return request.user.groups.filter(name='subscribers').exists()

