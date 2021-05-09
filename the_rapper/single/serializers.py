from rest_framework import serializers
from .models import Single


class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single
        fields = "_all_"


class SingleSerializerSave(serializers.ModelSerializer):
    class Meta:
        model = Single
        fields = ['name', 'view', 'artist_id']
