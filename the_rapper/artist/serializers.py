from rest_framework import serializers
from .models import Artist

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "_all_"

class ArtistSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ['aka', 'name', 'age']