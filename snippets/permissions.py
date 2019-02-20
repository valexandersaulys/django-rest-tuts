from rest_framework import permissions

class IsOwnerOrReadyOnly(permissions.BasePermission):
    '''
    Custom permissiont to only allow owners of an object to edit it
    '''
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
