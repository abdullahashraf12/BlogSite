# permissions.py
from rest_framework import permissions
from django.shortcuts import redirect

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # If the request method is DELETE, check ownership
        elif request.method == 'DELETE':
            # If the user is authenticated, check if they are the owner
            if request.user.is_authenticated:
                return obj.author.user == request.user
            # If the user is not authenticated, raise a permission denied error
            else:
                return False  # Return False instead of redirecting

        # For other request methods (PUT, PATCH, etc.), we allow read-only access
        return True

# class IsOwnerOrReadOnly(permissions.BasePermission):
#     """
#     Custom permission to only allow owners of an object to delete it.
#     """
#     def has_object_permission(self, request, view, obj):
#         # Read permissions are allowed to any request
#         # Always allow GET, HEAD, or OPTIONS requests
#         if request.method in permissions.SAFE_METHODS:
#             return True

#         # If the user is authenticated, check ownership
#         if request.user.is_authenticated:
#             return obj.author.user == request.user.profile

#         # If the user is not authenticated (anonymous user)
#         # Redirect them to the home page
#         else:
#             return redirect('blogApp:home')