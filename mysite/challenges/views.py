from django.shortcuts import render
from django.http import HttpResponse
from .models import challenge
from accounts.models import Player

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


def leaderboard(request):
    context = {
        'Players': Player.objects.all().order_by('-points')
    }
    return render(request, "challenges/leaderboard.html", context)


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
