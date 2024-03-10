from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.challengesHome, name="challenges-home"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path("<int:challenge_id>/", views.challengeIndi, name="challengeIndi"),
    path("challe/", views.challengesWithLocation, name="challengeWithLocation"),
    path("fox/", views.fox, name="fox"),
    path("foxCollection/", views.foxCollection, name="foxCollection")

    #path('', views.verify_player_location, name='verify_location'),
    #path('', views.user_location, name='user_location')
]