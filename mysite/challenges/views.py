from django.shortcuts import render
from django.http import HttpResponse
from .models import challenge

def challengesHome(request):
    context = {
        'challenges': challenge.objects.all()
    }
    return render(request, "challenges/challenges.html", context)