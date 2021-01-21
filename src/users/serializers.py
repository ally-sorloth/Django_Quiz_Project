from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator 
from django.contrib.auth.password_validation import validate_password


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, )
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password",
            "password2"
        )