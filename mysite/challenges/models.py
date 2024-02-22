from django.db import models

# Create your models here.
class challenge(models.Model):
    title = models.CharField(max_length=1000)
    content = models.TextField()
    # location
    points = models.IntegerField()
    cType = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


class userschallenges(models.Model):
    user = models.ForeignKey(Player, on_delete=models.CASCADE)
    challenge = models.ForeignKey(challenge, on_delete=models.CASCADE)
    date = models.DateField()
