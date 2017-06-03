from django.db import models
from fish.models import Fish

class Bundesland(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Mindestmass(models.Model):
    fish = models.ForeignKey(Fish)
    bundesland = models.ForeignKey(Bundesland)
    size = models.IntegerField()

class Schonzeit(models.Model):
    fish = models.ForeignKey(Fish)
    bundesland = models.ForeignKey(Bundesland)
    start = models.DateField()
    end = models.DateField()