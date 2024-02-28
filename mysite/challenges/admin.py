from django.contrib import admin

# Register your models here.
# from .models import challenge

# from django.contrib.gis.admin import OSMGeoAdmin
from .models import challenge, userschallenges
from accounts.models import Player
from django.contrib.gis.admin import GISModelAdmin



#admin.site.register(challenge)
admin.site.register(Player)
admin.site.register(userschallenges)

@admin.register(challenge)
class challengeAdmin(GISModelAdmin):
    list_display = ('title', 'location')
