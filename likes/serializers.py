from django.db import IntegrityError
from rest_framework import serializers
from .models import Likes

class LikeSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = '__all__'

    def create(self, validated_data):
        try:
            # super() is used to call the create method of the parent class
            # in this case, ModelSerializer
            return super().create(validated_data)
        except IntegrityError as err:
            raise serializers.ValidationError({
                'detail': 'It seems like you already liked this post'
            }) from err