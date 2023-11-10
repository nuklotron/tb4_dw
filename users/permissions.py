from rest_framework.permissions import BasePermission


class IsSuper(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if str(request._user) == obj.phone:
            return True
        return False
