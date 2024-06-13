import sys

from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'
    
    def ready(self):
        if 'runserver' not in sys.argv:
            return True
        
        from script.create_json_file import input_data
        from script.update_db_from_file import parse_json_file
        from weather.serializers import LocationSerializer
        from weather.models import Locations
        
        if input_data(10):
            location_data = parse_json_file()
            for data in location_data:
                Locations.objects.create(
                    location=data['location'],
                    timestamp=data['timestamp'],
                    temperature=data['temperature'],
                    humidity=data['humidity'],
                    description=data['description'],
                )
        
        return True
    
        
