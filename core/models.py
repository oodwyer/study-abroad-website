from django.db import models, migrations
from django.contrib.auth.models import User
import os
from django.db.models import signals
from django.conf import settings
from whoosh import fields
from whoosh import index
from whoosh.fields import Schema, TEXT, KEYWORD, ID, STORED
from whoosh.analysis import StemmingAnalyzer
import os, os.path
from whoosh import index

# Create your models here.
class Migration(migrations.Migration):
    atomic = False

class Place(models.Model): 
    name = models.CharField(max_length=140)

    def __str__(self):
        return self.name

class FoodReview(models.Model): 
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)
    price = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.body

class TourReview(models.Model): 
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)
    price = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.body

class StayReview(models.Model): 
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)
    price = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, blank=True, null=True)


    #magic method! 
    def __str__(self):
        return self.body

    def __ge__(x):
        if self.rating >= x.rating:
            return True 
        else: 
            return False 