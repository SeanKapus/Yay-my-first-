from django.contrib import admin

# Register your models here.
from django.contrib import admin
from game.models import Tournament, Group, Team, Player


admin.site.register(Tournament)
admin.site.register(Group)
admin.site.register(Team)
admin.site.register(Player)