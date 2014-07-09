from django.db import models

# Create your models here.

class Series(models.Model):
    series_name = models.CharField(max_length=120)
    series_type = models.CharField(max_length=120)
    Team = models.ForeignKey(Team, related_name='series')

     def __unicode__(self):
        return u"{}".format(self.title)


class Team(models.Model):
    team_name = models.CharField(max_length=120)
    team_car = models.CharField(max_length=120)

    def __unicode__(self):
        return u"{}".format(self.title)


class Driver(models.Model):
    driver_name = models.CharField(max_length=120)

    def __unicode__(self):
        return u"{}".format(self.title)



