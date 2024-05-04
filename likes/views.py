from rest_framework import generics, permissions
from .models import Likes
from .serializers import LikeSerializer
from api_positive.permissions import IsOwnerOrReadOnly
from django.db.models import Count, Q
from posts.models import Post
from posts.serializers import PostLikesSerializer
from rest_framework.response import Response
from rest_framework import status


class LikeList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer =self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        post_id = request.data.get('post')
        post = Post.objects.annotate(
        num_tops=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='top')
            ),
        num_likes=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='like')
            ),
        num_dislikes=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='dislike')
            )
        ).get(id=post_id)
        serialized_data = PostLikesSerializer(post)
        return Response(serialized_data.data, status=status.HTTP_201_CREATED, headers=headers)

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        post_id = instance.post.id
        self.perform_destroy(instance)
        post = Post.objects.annotate(
        num_tops=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='top')
            ),
        num_likes=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='like')
            ),
        num_dislikes=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='dislike')
            )
        ).get(id=post_id)
        serialized_data = PostLikesSerializer(post)
        return Response(serialized_data.data, status=status.HTTP_204_NO_CONTENT)
