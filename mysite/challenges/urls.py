from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.challengesHome, name="challenges-home"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path("<int:challenge_id>/", views.challengeIndi, name="challengeIndi")
    
]