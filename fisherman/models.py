from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from fish.models import Fish
from water.models import Water
from cal.models import Comment

class FisherMan(models.Model):
    account = models.ForeignKey(User)
    country = CountryField()

    def __str__(self):
        return self.account.username

class Catch(models.Model):
    fisherman = models.ForeignKey(FisherMan)
    fish = models.ForeignKey(Fish)
    size = models.IntegerField()
    weight = models.IntegerField()
    image = models.ImageField()
    water = models.ForeignKey(Water)
    date = models.DateField()
    time = models.TimeField()
    comments = models.ManyToManyField(Comment)

    def __str__(self):
        return '%s %s %s %s' % (self.fish.name, self.fisherman.account.username, self.date, self.water)