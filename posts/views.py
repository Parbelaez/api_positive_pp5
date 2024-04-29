from rest_framework import generics, permissions, filters, authentication
from .models import Post
from .serializers import PostSerializer
from api_positive.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Count, Q



class PostList(generics.ListCreateAPIView):
    """
    List all posts, or create a new post when authenticated.
    The perform_create method is used to set the owner of the post to the
    current user.
    """
    # authentication = authentication.TokenAuthentication
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().annotate(
        # In previous versions of Django, we would have to use the
        #Case When statement. After Django 3.2, we can use the Count
        #function with the filter parameter to count the number of
        #likes of each type.
        num_tops=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='top')
            ),
        num_likes=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='like')
            ),
        num_dislikes=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='dislike')
            )
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
        ]
    filterset_fields = [
        'owner__profile',
        'place',
        'post_likes__owner__profile',
    ]
    search_fields = ['post_place__place_name', 'post_place__country', 'post_place__city']
    ordering_fields = ['post_place__place_name',
        'post_place__city', 'post_place__country', 'created_at'
        ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a post instance when authenticated and owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.annotate(
        num_tops=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='top')
            ),
        num_likes=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='like')
            ),
        num_dislikes=Count('post_likes__like_type',
            filter=Q(post_likes__like_type='dislike')
            )
    ).order_by('-created_at')
    serializer_class = PostSerializer

