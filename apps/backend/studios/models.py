from django.contrib.gis.db import models
from django.contrib.auth.models import User

class Studio(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.PointField(null=True, blank=True)
    max_capacity = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    @property
    def location_geojson(self):
        if self.location:
            return {
                "type": "Point",
                "coordinates": [self.location.x, self.location.y]
            }
        return None


    def __str__(self):
        return self.description



class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    reserved_from = models.DateTimeField()
    reserved_to = models.DateTimeField()
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
