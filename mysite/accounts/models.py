from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return self.user.username



class GameKeeper(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
