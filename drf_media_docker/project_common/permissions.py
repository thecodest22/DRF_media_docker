from django.contrib.auth.models import Group

from rest_framework.permissions import BasePermission


class IsSubscriber(BasePermission):
    def has_permission(self, request, view):
        """Returns True if the User is in the 'subscribers' Group"""
        try:
            return Group.objects.get(name='subscribers').user_set.filter(id=request.user.id).exists()
        except Group.DoesNotExist:
            return False
