from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Board , Task


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


class CreatBoardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Board
		exclude = ['owner', 'id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class BoardsSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Board
        fields = ['title', 'owner', ]


# ---- new ----

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['creation_date', 'description', 'is_hidden', 'is_done',]	


class BoardOwnerDetailSerializer(serializers.ModelSerializer):
	tasks = serializers.SerializerMethodField()
	class Meta:
		model = Board
		fields = ['title', 'tasks']
		
	def get_tasks(self, obj):
		return TaskSerializer(obj.tasks.all(), many=True).data


class BoardDetailSerializer(serializers.ModelSerializer):
	tasks = serializers.SerializerMethodField()
	class Meta:
		model = Board
		fields = ['title', 'tasks']
			
	def get_tasks(self, obj):
		return TaskSerializer(obj.tasks.filter(is_hidden=False), many=True).data


class CreateUpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'is_hidden', 'is_done',]

# ---- end new ----
