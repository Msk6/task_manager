from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Board , Task


class CreatBoardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Board
		exclude = ['owner',]

class BoardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['title', 'owner', ]
