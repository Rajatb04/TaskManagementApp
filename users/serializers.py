from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'mobile']
        extra_kwargs = {
            'email': {'required': True},
            'name': {'required': True}
        }

    def create(self, validated_data):
        """
        Create and return a new User instance
        """
        return User.objects.create(**validated_data)