from rest_framework import serializers

from accounts.models import User
from accounts.models import TrainerProfile
from accounts.models import StudentProfile

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["username","email","password","phone","role"]

        read_only_fields =["id"]

    def create(self,validated_data):

        return User.objects.create_user(**validated_data)

class TrainerProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model=TrainerProfile

        fields="__all__"

        read_only_flelds=['user']

class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model=StudentProfile

        fields="__all__"

        read_only_flelds=['user']