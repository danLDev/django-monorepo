from rest_framework import serializers
from .models import Studio, Booking
from django.contrib.auth.models import User

class StudioSerializer(serializers.ModelSerializer):
    location_geojson = serializers.ReadOnlyField()
    
    class Meta:
        model = Studio
        fields = ['id', 'description', 'created_at', 'location_geojson', 'max_capacity', 'image_url', 'owner']
    


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']



class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'reserved_from', 'reserved_to', 'studio', 'user']