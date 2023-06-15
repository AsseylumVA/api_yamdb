from rest_framework import permissions

from users.permissions import IsAdmin as Admin_Perm


class IsAdminOrModer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_moderator or request.user.is_admin


class ReviewPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return request.method in permissions.SAFE_METHODS or (
            obj.author == request.user or request.user.is_moderator)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_admin)

    def has_object_permission(self, request, view, obj):
        return request.user.is_admin


class IsAdmin(Admin_Perm):
    pass
