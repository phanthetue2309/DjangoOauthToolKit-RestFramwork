from rest_framework import generics, permissions, serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
