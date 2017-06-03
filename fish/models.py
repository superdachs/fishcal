from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=255)
    lat_name = models.CharField(max_length=255)
    image = models.ImageField()

    def __str__(self):
        return '%s (%s)' % (self.name, self.lat_name)
