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
            'groups',
            'user_permissions',
            'last_login',
            'date_joined',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data, is_active=False)
        register = Register.objects.create(user=user)
        register.send_registration_mail()
        return user


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = '__all__'
