from rest_framework import permissions
import ipdb


class IsUserOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # ipdb.set_trace()
        if view.kwargs["user_id"] == request.user.id:
            return True
        if request.user.is_superuser:
            return True
        return False
