from django.shortcuts import render
from django.http import HttpResponse
from .models import challenge, userschallenges
from accounts.models import Player
import datetime

from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def challengesHome(request):
    context = {
        'challenges': challenge.objects.all()
    }
    return render(request, "challenges/challenges.html", context)

def challengesWithLocation(request):
    context = {
        'challenges': challenge.objects.all()
    }
    return render(request, "challenges/individualchallenge.html", context)

def userProfile(request):
    current_user = request.user
    current_player = Player.objects.get(pk=current_user.id)
    context = {
            'userschallenges': userschallenges.objects.filter(user=current_player),
            'player': current_player
    }
    return render(request,"challenges/userprofile.html",context)

def leaderboard(request):
    context = {
        'Players': Player.objects.all().order_by('-points')
    }
    return render(request, "challenges/leaderboard.html", context)

def fox(request):
    context = {
        'challenges': challenge.objects.all()
    }
    return render(request, "challenges/fox.html", context)

def foxCollection(request):
    context = {
        'challenges': challenge.objects.all()
    }
    return render(request, "challenges/foxCollection.html", context)


def verify_player_location(request):
    player_location = Point(float(request.POST['longitude']), float(request.POST['latitude']), srid=4326)
    challenge = challenge.objects.annotate(distance=Distance('location', player_location)).filter(distance__lte=D(m=20)).first() #m is distance radius in meters

    if challenge:
        
        return JsonResponse({'status': 'success', 'message': 'Challenge completed!'})
    else:
        return JsonResponse({'status': 'failure', 'message': 'Not close enough to the challenge location.'})


@csrf_exempt
def user_location(request):
    if request.method == 'POST':
        data = request.json()
        latitude = data['latitude']
        longitude = data['longitude']
        
        # Example: Save the location to the database
        # Assuming you have a model with a GeoDjango PointField
        user_location = Point(longitude, latitude)
        # Save user_location to a model instance, for example
        # challenge.objects.create(location=user_location)
        # print(user_location)
        
        return JsonResponse({"success": "Location received successfully."})

    return JsonResponse({"error": "This endpoint only supports POST requests."})


def challengeIndi(request, challenge_id):
    current_user = request.user
    context = {
        'challenge': challenge.objects.get(pk=challenge_id),
        'complete': False,
        'otherplayers': (userschallenges.objects.filter(challenge=challenge.objects.get(pk=challenge_id))).exclude(user = Player.objects.get(pk=current_user.id)),
    }
    
    if (current_user.is_authenticated):
        current_player = Player.objects.get(pk=current_user.id)
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
        if ((current_user.is_authenticated) and (challenge_id == 3)):
            return render(request, "challenges/fox.html",context)
    return render(request, "challenges/challenge.html",context)