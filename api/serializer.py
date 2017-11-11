from django.contrib.auth import update_session_auth_hash
from rest_framework import serializers

from .models import Account, AccountManager, Group, Homework

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = Account
        fields = ("userID", "username", "password", "loginType")

    def create(self, validated_data):
        return Account.objects.create_user(request_data=validated_data)

class GroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("id", "name")

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("userID", "username")

class GroupDetailSerializer(serializers.ModelSerializer):
    member = MemberSerializer(many= True)

    class Meta:
        model = Group
        fields = ("name", "id", "joincode", "member")

class AddMemberSerializer(serializers.Serializer):
    joincode = serializers.CharField(max_length=255)

class CreateGroupSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)

class HomeworkListSerializer(serializers.ModelSerializer):
    group = GroupListSerializer()

    class Meta:
        model = Homework
        fields = ("id", "group", "deadline", "name")

