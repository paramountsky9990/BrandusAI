from rest_framework import serializers
from .models import UserSocialData

class UserSocialDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSocialData
        fields = ['id', 'user', 'platform', 'data', 'access_token']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Optionally, hide access_token in the response if needed
        representation.pop('access_token', None)
        return representation
