from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView

from django.contrib.auth.models import User
from .models import Board , Task
from .serializers import CreatBoardSerializer,
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BoardCreate(CreateAPIView):
    serializer_class = CreatBoardSerializer
    permission_classes= [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class BoardsList(ListAPIView):
	queryset = Board.objects.all()
	serializer_class = BoardsSerializer
	permission_classes= [IsAuthenticated]
