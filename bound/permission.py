from rest_framework import permissions


class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin()


    def has_object_permission(self, request, view, obj):
        return request.user.is_admin()

class CustomerOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_customer()


    def has_object_permission(self, request, view, obj):
        return request.user.is_customer()

class DriverOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_driver()


    def has_object_permission(self, request, view, obj):
        return request.user.is_driver()
