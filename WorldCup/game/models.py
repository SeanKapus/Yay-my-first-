from django.db import models

# Create tournament
class Tournament(models.Model):
    year = models.IntegerField()
    host_country = models.CharField(max_length=120)


# Create groups
class Group(models.Model):
    group_name = models.CharField(max_length=10)
    Tournament = models.ForeignKey(Tournament, related_name='group')

    def __unicode__(self):
        return u"{}".format(self.title)


# create Team
class Team(models.Model):
    team_name = models.CharField(max_length=120)
    team_country = models.CharField(max_length = 120)
    Group = models.ForeignKey(Group, related_name='team')

    def __unicode__(self):
        return u"{}".format(self.title)


# Create your players here.
class Player(models.Model):
    Player_name = models.CharField(max_length=120)
    Forward = models.CharField(max_length=120)
    Midfield = models.CharField(max_length=100)
    Defense = models.CharField(max_length=120)
    Team = models.ForeignKey(Team, related_name='player')

    def __unicode__(self):
        return u"{}".format(self.username)









