from django.db import models, migrations
from django.contrib.auth.models import User

# Create your models here.
class Migration(migrations.Migration):
    atomic = False

class FoodReview(models.Model): 
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)
    price = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)

class TourReview(models.Model): 
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)
    price = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)

class StayReview(models.Model): 
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now=True)
    num_likes = models.IntegerField(default=0)
    price = models.IntegerField(default = 0)
    rating = models.IntegerField(default = 0)

class Place(models.Model): 
    name = models.CharField(max_length=140)
    food = models.ManyToManyField(FoodReview, blank=True)
    tour = models.ManyToManyField(TourReview, blank=True)
    stay = models.ManyToManyField(StayReview, blank=True)