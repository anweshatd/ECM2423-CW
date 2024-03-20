from django.db import models

from accounts.models import Player

from django.contrib.gis.db import models

# Create your models here.
class challenge(models.Model):
    TYPE_CHOICES = (
        ('Location-Based', 'Location-Based'),
        ('Non Location-Based', 'Non Location-Based'),
    )

    title = models.CharField(max_length=1000)
    content = models.TextField()
    # location
    points = models.IntegerField()

    cType = models.CharField(max_length=100, choices=TYPE_CHOICES)

    location = models.PointField(blank=True, null=True)
    
    badge = models.CharField(max_length=5, default='0') #emoji for badge
    
    def __str__(self):
        return self.title


class userschallenges(models.Model):
    user = models.ForeignKey(Player, on_delete=models.CASCADE)
    challenge = models.ForeignKey(challenge, on_delete=models.CASCADE)
    date = models.DateField()