from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Create your models here.




class Ing(models.Model):
    name = models.CharField(max_length=300)
    type = models.CharField(max_length=300)
    family = models.CharField(max_length=300)
    kcal = models.IntegerField()
    description = models.TextField()





