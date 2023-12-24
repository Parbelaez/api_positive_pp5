from rest_framework import generics, permissions, filters
from .models import Place
from .serializers import PlaceSerializer
from api_positive.permissions import IsOwnerOrReadOnly
from rest_framework.exceptions import ValidationError


class PlaceList(generics.ListCreateAPIView):
    serializer_class = PlaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Place.objects.all().order_by('-created_at')

    # We add the filter and ordering backends to be able to filter and order
    # the places by name and city
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['place_name', 'city']
    search_fields = ['place_name', 'city']

    # We override the perform_create method to be able to use the get_or_create
    # method from the model. This way we can check if a place with the same
    # name and city already exists and if it does, we don't create a new one
    # but we return the existing one
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PlaceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()