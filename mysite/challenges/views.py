from django.shortcuts import render
from django.http import HttpResponse
from .models import challenge, userschallenges
from accounts.models import Player
import datetime

def challengesHome(request):
    context = {
        'challenges': challenge.objects.all()
    }
    return render(request, "challenges/challenges.html", context)


def leaderboard(request):
    context = {
        'Players': Player.objects.all().order_by('-points')
    }
    return render(request, "challenges/leaderboard.html", context)


def challengeIndi(request, challenge_id):
    context = {
        'challenge': challenge.objects.get(pk=challenge_id),
        'complete': False
    }
    current_user = request.user
    if (current_user.is_authenticated):
        current_player = Player.objects.get(pk=current_user.id) #need to update sign up page btw
        try:
            uc = userschallenges.objects.get(user=current_player,challenge=context['challenge'])
            context.update({'complete': True})
        except userschallenges.DoesNotExist:
            uc = None
        if (request.method == "POST"):
            if uc:  #check if user has already completed challenge
                return HttpResponse("You have already completed this challenge")
            #update user points
            current_player.points += context['challenge'].points
            current_player.save()
            #add to user-challenge database
            today = datetime.date.today()
            link = userschallenges(user=current_player,challenge=context['challenge'],date=today)
            link.save() 
            return render(request, "challenges/challenge_complete.html",context)
    return render(request, "challenges/challenge.html",context)
