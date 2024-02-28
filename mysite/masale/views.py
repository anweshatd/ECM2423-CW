from django.shortcuts import render
#from django.http import HttpResponse
from accounts.models import Player


def home(request):
    current_user = request.user
    if (current_user.is_authenticated): #will create a new player if it doesn't exist
        try:
            current_player = Player.objects.get(pk=current_user.id) 
        except Player.DoesNotExist:
            newPlayer = Player(user=current_user,points=0)
            newPlayer.save() 

    return render(request, "home.html")
