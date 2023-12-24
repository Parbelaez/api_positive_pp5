from rest_framework import serializers
from .models import Post
from likes.models import Likes
from datetime import datetime


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    # We will use the Method Field to realte if the logged user has liked
    # the post or not, and the type of like
    like_type = serializers.SerializerMethodField()
    num_tops = serializers.ReadOnlyField()
    num_likes = serializers.ReadOnlyField()
    num_dislikes = serializers.ReadOnlyField()

    # To optimize the resources usage, we need to set some image validations
    # to avoid sending the image to cloudinary if it is not compliant with
    # our requirements of size and format

    def validate_image(self, value):
        # We check if the image is bigger than 2MB
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'The maximum file size that can be uploaded is 2MB'
                )
        # We validate if the image width is bigger than 4096px
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'The maximum width allowed is 4096px'
                )
        # We validate if the image height is bigger than 4096px
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'The maximum height allowed is 4096px'
                )
        # We validate if the image format is not supported
        if value.content_type not in ['image/jpeg', 'image/png']:
            raise serializers.ValidationError(
                'The allowed formats are JPEG and PNG'
                )
        # We return the value if it is compliant with our requirements
        return value

    def validate_visit_date(self, value):
        # We check if the date is in the future
        if value > datetime.now().date():
            raise serializers.ValidationError(
                'The visit date cannot be in the future'
                )
        # We return the value if it is compliant with our requirements
        return value

    def get_is_owner(self, obj):
        return self.context['request'].user == obj.owner

    # We need to define the get_like_id method to be able to access the
    # like_id field in the serializer
    def get_like_type(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Likes.objects.filter(
                owner=user, post=obj
            ).first()
            return like.like_type if like else None
        return None

    class Meta: 
        model = Post
        fields = [
            ## the id field is created automatically by django
            ## but we need to declare it here to be able to access it
            'id',
            'owner',
            'is_owner',
            'profile_id',
            'profile_image',
            'created_at',
            'updated_at',
            'place',
            'visit_date',
            'title',
            'content',
            'image',
            'image_filter',
            'recommendation',
            # Type of like that the logged user has given to the post
            'like_type',
            # Count of like_types
            'num_tops',
            'num_likes',
            'num_dislikes',
        ]