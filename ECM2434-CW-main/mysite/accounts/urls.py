from django.urls import path

from .views import SignUp


urlpatterns = [
    path("signup/", SignUp, name="signup"),
]