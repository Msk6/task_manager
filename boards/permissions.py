from rest_framework.permissions import BasePermission
from .models import Board


class IsOwner(BasePermission):
    message = "go away"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or (obj.owner == request.user):
            return True
        else:
            return False

# ---- new ----

# Work for all views
class EditBoard(BasePermission):
    message = "Sorry you are not the owner"

    def has_permission(self, request, view):
        board = Board.objects.get(id=view.kwargs['board_id'])
        return request.user.is_staff or board.owner == request.user


# Doesn't work for TaskAdd
class EditTask(BasePermission):
    message = "Sorry you are not the owner"

    def has_object_permission(self, request, view, obj):
        return obj.board.owner == request.user or request.user.is_staff

# ---- new ----
