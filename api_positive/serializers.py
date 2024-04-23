from dj_rest_auth.serializers import UserDetailsSerializer
from profiles.serializers import ProfileSerializer
from rest_framework import serializers


class CurrentUserSerializer(UserDetailsSerializer):
    profile = ProfileSerializer(read_only=True)
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile', 'profile_id', 'profile_image'
        )
