from django.contrib import admin

# Register your models here.
from .models import challenge
from accounts.models import Player

admin.site.register(challenge)
admin.site.register(Player)