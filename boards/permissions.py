from rest_framework.permissions import BasePermission
from .models import Board


# Work for all views (used one)
class EditBoard(BasePermission):
    message = "Sorry you are not the owner"

    def has_permission(self, request, view):
        board = Board.objects.get(id=view.kwargs['board_id'])
        return request.user.is_staff or board.owner == request.user



# ----- not used -----   
    
class IsOwner(BasePermission):
    message = "You must be the owner of this book."

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        else:
            return False


# Doesn't work for TaskAdd because the object doesn't exists until we create it (no error)
class EditTask(BasePermission):
    message = "Sorry you are not the owner"

    def has_object_permission(self, request, view, obj):
        return obj.board.owner == request.user or request.user.is_staff

# ----- end not used ----- 