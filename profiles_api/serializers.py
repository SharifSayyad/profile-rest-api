from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing our APIView """
    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        # fields = '__all__' to include all fields
        # exclude = ('id') to exclued some fields
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{'input_type':'password'}
            }
        }# for set password only write not for retrive
    def create(self, validated_data):
        """ create method override because need to store password encripted """
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class ProfileFeedSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile':{'read_only':True}}
