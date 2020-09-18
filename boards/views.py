from django.shortcuts import render
from rest_framework.generics import (
	ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
	)
from .serializers import (
	RegisterSerializer, CreatBoardSerializer, BoardsSerializer, 
	BoardDetailSerializer, BoardOwnerDetailSerializer, CreateUpdateTaskSerializer
	)
from django.contrib.auth.models import User
from .models import Board, Task

from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner, EditTask, EditBoard


class Register(CreateAPIView):
    serializer_class = RegisterSerializer


class BoardCreate(CreateAPIView):
    serializer_class = CreatBoardSerializer
    permission_classes= [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BoardsList(ListAPIView):
	queryset = Board.objects.all()
	serializer_class = BoardsSerializer
	permission_classes= [IsAuthenticated, IsOwner]


class BoardDelete(DestroyAPIView):
	queryset = Board.objects.all()
	lookup_field = 'id'
	lookup_url_kwarg = 'board_id'
	permission_classes= [EditBoard]

# ---- new ----

class BoardDetail(RetrieveAPIView):
	queryset = Board.objects.all()
	serializer_class = BoardDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'board_id'
	permission_classes = [IsAuthenticated]

	# control the including of hidden tasks 
	def get_serializer_class(self):
		if self.request.user == self.get_object().owner or self.request.user.is_staff:
			return BoardOwnerDetailSerializer
		elif self.request.user.is_authenticated:
			return BoardDetailSerializer


class TaskAdd(CreateAPIView):
	serializer_class = CreateUpdateTaskSerializer
	permission_classes= [EditBoard]
	
	def perform_create(self, serializer):
		serializer.save(board_id=self.kwargs['board_id'])


class TaskUpdate(RetrieveUpdateAPIView):
	queryset = Task.objects.all()
	serializer_class = CreateUpdateTaskSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'task_id'
	permission_classes= [EditBoard]

# ---- end new ----
