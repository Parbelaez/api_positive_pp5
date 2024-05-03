from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.permissions import IsAuthenticated
from api_positive.permissions import IsOwnerOrReadOnly
from  django.db.models import Count

# We have refactored this part of the code to use generics
# not only because it is shorter, but also because it is more
# readable and easier to understand, mostly, when we are using
# the annotate function to be able to count the number of posts
# of each profile, and how many places they have visited

class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view ass porodile creation is handled by django signals
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.all().annotate(
        num_posts=Count('owner__post', distinct=True),
        num_places=Count('owner__place', distinct=True),
        limit = self.request.query_params.get('limit', None)
        if limit:
            return self.queryset[:int(limit)]
        return self.queryset
        ).order_by('-created_at')
    filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['num_posts', 'num_places']

class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve, update or delete a profile instance.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        num_posts=Count('owner__post', distinct=True),
        num_places=Count('owner__place', distinct=True)
    ).order_by('-created_at')
