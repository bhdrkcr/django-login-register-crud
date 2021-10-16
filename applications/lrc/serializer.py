# Third Party
from rest_framework import serializers

# Local Folder
# Local Folderry
from .models import Register, User

__all__ = ['UserSerializer', 'RegisterSerializer']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'is_superuser',
            'is_staff',
            'is_active',
            'is_validated',
            'email',
            'groups',
            'user_permissions',
            'last_login',
            'date_joined',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.is_validated = validated_data.get('is_validated', instance.is_validated)
        instance.set_password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
        read_only_fields = (
            'uuid',
            'user_id',
        )

    def create(self, validated_data):
        return Register.objects.create(**validated_data)
