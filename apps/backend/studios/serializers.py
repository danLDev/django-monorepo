from rest_framework import serializers
from .models import Studio

class StudioSerializer(serializers.ModelSerializer):
    location_geojson = serializers.ReadOnlyField()
    
    class Meta:
        model = Studio
        fields = ['id', 'description', 'created_at', 'location_geojson', 'max_capacity', 'image_url']
    
