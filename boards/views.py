from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

from django.contrib.auth.models import User
from .models import Board , Task
from .serializers import RegisterSerializer, CreatBoardSerializer, BoardsSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner

# Create your views here.

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
