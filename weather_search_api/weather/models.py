from uuid import uuid4

from django.db import models

class Locations(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    location = models.CharField(max_length=255)
    timestamp = models.DateTimeField()
    temperature = models.DecimalField(max_digits=6, decimal_places=3)
    humidity = models.DecimalField(max_digits=6, decimal_places=3)
    description = models.CharField(max_length=255)
    
