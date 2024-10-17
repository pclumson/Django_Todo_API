
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from todo.models import Task



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
