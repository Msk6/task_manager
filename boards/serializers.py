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
        fields = ['first_name', 'last_name','username' ]


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
	hidden = serializers.SerializerMethodField()
	done = serializers.SerializerMethodField()
	not_done = serializers.SerializerMethodField()
	class Meta:
		model = Board
		fields = ['title', 'hidden', 'done', 'not_done']

	def get_hidden(self, obj):
		return TaskSerializer(obj.tasks.filter(is_hidden=True).order_by('creation_date'), many=True).data

	def get_done(self, obj):
		return TaskSerializer(obj.tasks.filter(is_done=True).order_by('creation_date'), many=True).data

	def get_not_done(self, obj):
		return TaskSerializer(obj.tasks.filter(is_done=False).order_by('creation_date'), many=True).data


class BoardDetailSerializer(serializers.ModelSerializer):
	done = serializers.SerializerMethodField()
	not_done = serializers.SerializerMethodField()
	class Meta:
		model = Board
		fields = ['title', 'done','not_done']

	def get_done(self, obj):
		return TaskSerializer(obj.tasks.filter(is_done=True,is_hidden=False).order_by('creation_date'), many=True).data
	def get_not_done(self, obj):
		return TaskSerializer(obj.tasks.filter(is_done=False,is_hidden=False).order_by('creation_date'), many=True).data


class CreateUpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['description', 'is_hidden', 'is_done',]

# ---- end new ----
