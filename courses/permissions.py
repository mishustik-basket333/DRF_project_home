from rest_framework.permissions import BasePermission


class IsModeratorPermission(BasePermission):
    def has_permission(self, request, view):

        if request.user.is_staff:
            return True
        return False


class IsSuperUserPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False




