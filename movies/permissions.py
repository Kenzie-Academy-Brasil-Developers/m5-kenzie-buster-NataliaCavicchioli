from rest_framework import permissions


class IsAdm(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_authenticated and request.user.is_superuser


# class IsUserOwner(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.user == request.user
