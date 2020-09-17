from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board , Task


class CreatBoardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Board
		exclude = ['owner',]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class BoardsSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Board
        fields = ['title', 'owner', ]


class RegisterSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	class Meta:
		model = User
		fields = ['username', 'password']

	def create(self, validated_data):
		username = validated_data['username']
		password = validated_data['password']
		new_user = User(username=username)
		new_user.set_password(password)
		new_user.save()
		return validated_data
