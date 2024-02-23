from django.contrib import admin

# Register your models here.
# from .models import challenge

# from django.contrib.gis.admin import OSMGeoAdmin
from .models import challenge

# @admin.register(challenge)
# class ChallengeAdmin(OSMGeoAdmin):
#     list_display = ('title', 'location')

admin.site.register(challenge)