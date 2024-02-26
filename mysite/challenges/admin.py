from django.contrib import admin

# Register your models here.
# from .models import challenge

# from django.contrib.gis.admin import OSMGeoAdmin
from .models import challenge
from accounts.models import Player
from django.contrib.gis.admin import OSMGeoAdmin


#admin.site.register(challenge)
admin.site.register(Player)

@admin.register(challenge)
class challengeAdmin(OSMGeoAdmin):
    list_display = ('title', 'location')
