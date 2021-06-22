from rest_framework import generics, permissions, serializers
from .models import Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instrument
        fields = '__all__'
