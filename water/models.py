from django.db import models
from django_countries.fields import CountryField

from cal.models import Bundesland


class Water(models.Model):
    name = models.CharField(max_length=255)
    ident = models.CharField(max_length=10)
    lat = models.FloatField()
    lon = models.FloatField()
    country = CountryField()
    bundesland = models.ForeignKey(Bundesland)

    def __str__(self):
        return '%s %s (%s)' % (self.ident, self.name, self.country.name)
