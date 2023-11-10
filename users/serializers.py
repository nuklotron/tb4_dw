from rest_framework import serializers
from users.models import User


class UserDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('phone',)


class UserSerializer(serializers.ModelSerializer):

    invited_users = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('phone', 'email', 'first_name', 'last_name', 'invite_code', 'invited', 'invited_users',)

    def get_invited_users(self, obj):
        """
        If user invited other users it would be in custom field - invited_users
        """
        users_data = User.objects.filter(invited=obj.invite_code)
        return UserDataSerializer(users_data, many=True).data
