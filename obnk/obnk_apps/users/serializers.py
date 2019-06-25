# Rest-framework imports
from rest_framework import serializers

# OBnk
from models import User
from response_texts import get_response_text, USER_NOT_EXISTS, LOGIN_ERROR


class AuthTokenEmailSerializer(serializers.Serializer):

    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = User.objects.filter(email=attrs.get("email"))
        if not user:
            raise serializers.ValidationError(get_response_text(
                USER_NOT_EXISTS))
        else:
            if not user[0].check_password(attrs.get("password")):
                raise serializers.ValidationError(get_response_text(
                    LOGIN_ERROR))
        return attrs


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        read_only_fields = ["uuid"]
        exclude = ("password", "is_superuser", "is_active", "is_staff",
                   "groups", "user_permissions", "last_login")

    def update(self, instance, validated_data):
        for (key, value) in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
