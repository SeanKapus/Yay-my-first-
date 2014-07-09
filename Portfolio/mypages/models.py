from django.db import models


class Home(models.Model):
    name = models.CharField(max_length=120)
    twitter = models.CharField(max_length=40, null=True)

    def __unicode__(self):
        return u"{}".format(self.name)


class About(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name