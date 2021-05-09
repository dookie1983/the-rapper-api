from rest_framework import viewsets, status
from .models import Artist
from .serializers import ArtistSerializer, ArtistSerializerSave
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ArtistViewSet(viewsets.ModelViewSet):
    @api_view(['GET'])
    def all(self, format=None):
        if self.method == 'GET':
            artists = Artist.objects.all();
            artists_serializer = ArtistSerializer(artists, many=True)
            return Response(artists_serializer.data)

    @api_view(['POST'])
    def create(self):
        if self.method == 'POST':
            artists_serializer = ArtistSerializerSave(data=self.data, many=False)
            if artists_serializer.is_valid():
                artists_serializer.save()
                return Response(artists_serializer.data, status=status.HTTP_201_CREATED)
            return Response(artists_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
