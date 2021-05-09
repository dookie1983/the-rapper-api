from rest_framework import viewsets, status
from .models import Artist
from .serializers import ArtistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ArtistViewSet(viewsets.ModelViewSet):
    @api_view(('GET',))
    def all(request, format=None):
        if request.method == 'GET':
            artists = Artist.objects.all()
            # artists_serializer = ArtistSerializer(artists, many=True)
            # return Response(artists_serializer)
            return Response(artists)
