from django.contrib.auth import authenticate
from rest_framework import serializers

from users.models import CustomUser


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')

    def validate(self, attrs):
        try:
            user = CustomUser.objects.get(email=attrs['email'])
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError('Неправильные учетные данные')

        user = authenticate(email=user.email, password=attrs['password'])

        if user and user.is_active:
            return user

        raise serializers.ValidationError("Неправильные учетные данные")