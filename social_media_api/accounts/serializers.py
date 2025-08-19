from rest_framework import serializers
from django.contrib.auth import authenticate, get_user_model
# from .models import CustomUser
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RegistrationSerializser(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    token = serializers.CharField(read_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        token = Token.objects.create(user=user)
        user.token = token.key
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, attrs):
        user = authenticate(username = attrs['username'], password = attrs['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Wrong credentials")