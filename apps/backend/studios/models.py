from django.contrib.gis.db import models


class Studio(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.PointField(null=True, blank=True)
    max_capacity = models.IntegerField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)

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
