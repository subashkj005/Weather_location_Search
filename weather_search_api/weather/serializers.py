from rest_framework import serializers

from .models import Locations

class LocationSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Locations
        fields = ['location', 'timestamp', 'timestamp', 'temperature','humidity', 'description']
        
    