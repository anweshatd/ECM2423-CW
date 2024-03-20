# @author Lucas and Alex

from django.urls import include,path
from . import views


urlpatterns = [
    path('', views.challengesHome, name="challenges-home"),
    path('leaderboard/', views.leaderboard, name="leaderboard"),
    path("fox/",views.fox,name="fox"),
    path("<int:challenge_id>/", views.challengeIndi, name="challengeIndi"),
    path("challe/", views.challengesWithLocation, name="challengeWithLocation"),
    path("userProfile/",views.userProfile,name="userProfile"),
    path("foxCollection/",views.foxCollection,name="foxCollection"),
    path('upload/', views.challengeIndi)
    #path('', views.verify_player_location, name='verify_location'),
    #path('', views.user_location, name='user_location')
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)