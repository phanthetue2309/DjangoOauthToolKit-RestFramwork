from rest_framework import serializers
from accounts.models import User


class CreateUserSerializer(serializers.ModelSerializer):

    def save(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.create_user(email, password)
        return user

    class Meta:
        model = User
        fields = ['id', 'email', 'password']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
