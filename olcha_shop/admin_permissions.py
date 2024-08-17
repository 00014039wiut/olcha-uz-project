from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.owner == request.user:
            if request.method == "DELETE" and request.user.is_superuser:
                return True
            if request.method in ["PATCH", "PUT"] and request.user.is_superuser:
                return True
