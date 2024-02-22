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