from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from users.models import CustomUser


class CustomUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    last_login = serializers.DateTimeField(allow_null=True, required=False)
    email = serializers.EmailField(label='Email address', max_length=255,
                                   validators=[UniqueValidator(queryset=CustomUser.objects.all())])
    first_name = serializers.CharField(max_length=70, required=False)
    last_name = serializers.CharField(max_length=70, required=False)
    date_of_birth = serializers.DateField(allow_null=True, required=False)
    is_active = serializers.BooleanField(required=False)
    is_admin = serializers.BooleanField(required=False)
    created_at = serializers.DateTimeField(read_only=True)
    last_modified_at = serializers.DateTimeField(read_only=True)
    deleted = serializers.BooleanField(required=False)
    deleted_on = serializers.DateTimeField(allow_null=True, required=False)

    def create(self, validated_data):
        instance = CustomUser.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        CustomUser.objects.filter(id=instance.id).update(**validated_data)
        return CustomUser.objects.get(id=instance.id)
