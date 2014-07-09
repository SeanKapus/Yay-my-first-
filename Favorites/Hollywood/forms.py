__author__ = 'CatsAir'
from Hollywood.models import Genre, Movie, Actor
from django.forms import ModelForm


class GenreForm(ModelForm):
    class Meta:
        model = Genre


class MovieForm(ModelForm):
    class Meta:
        model = Movie


class ActorForm(ModelForm):
    class Meta:
        model = Actor
