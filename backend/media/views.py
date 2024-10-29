from rest_framework import viewsets
from .models import MediaItem, UserInteraction
from .serializers import MediaItemSerializer, UserInteractionSerializer

class MediaItemViewSet(viewsets.ModelViewSet):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer

class UserInteractionViewSet(viewsets.ModelViewSet):
    queryset = UserInteraction.objects.all()
    serializer_class = UserInteractionSerializer
