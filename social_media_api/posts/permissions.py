from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    # Allow only owners to edit their posts or comments
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS: # Allow read-only methods for everyone
            return True
        return getattr(obj, 'author_id', None) == getattr(request.user, 'id', None) # Check if the user is the author of the post or comment