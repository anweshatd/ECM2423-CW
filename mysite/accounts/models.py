from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField()
    badges = models.CharField(max_length=50, default=0)
    numChallenges = models.IntegerField() #number of challenges the user has completed

    def __str__(self):
        return self.user.username

