from django.shortcuts import render
from django.http import HttpResponse
from .models import challenge
from accounts.models import Player

def challengesHome(request):
    context = {
        'challenges': challenge.objects.all()
    }
    return render(request, "challenges/challenges.html", context)


def leaderboard(request):
    context = {
        'Players': Player.objects.all().order_by(points.desc())
    }
    return render(request, "challenges/leaderboard.html", context)