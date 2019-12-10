from django.shortcuts import render, redirect
from core.models import Place, FoodReview, StayReview, TourReview
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT 
import os.path 
from whoosh.index import create_in 
from haystack.query import SearchQuerySet

# Create your views here.

#main page 
def splash(request): 
    #if method is post, someone added new place 
    if request.method == "POST":
        #create new place 
        name = request.POST["name"].capitalize()
        p = Place.objects.create(name=name)
        #create URL name without spaces
        p.urlName = p.getUrlName()
        p.save()
        return redirect("/")
    else: 
        #otherwise, display all places alphabetically
        places = Place.objects.all().order_by('name')
        return render(request, "splash.html", {"places": places})

#place specific page
def place(request, urlName):
    #if someone submitted a new review, check for post request 
    if request.method == "POST": 
        #get fields from post request
        body = request.POST["name"]
        price = request.POST["price"]
        rating = request.POST["rating"]

        #get place object associated w it 
        p = Place.objects.get(urlName=urlName)

        #which type of review? check which button 
        if 'food' in request.POST:
            #create new review 
            f = FoodReview.objects.create(author=request.user, body=body, num_likes=0, price=price, rating=rating, place=p)
        elif 'stay' in request.POST: 
            s = StayReview.objects.create(author=request.user, body=body, num_likes=0, price=price, rating=rating, place=p)
        elif 'tour' in request.POST: 
            t = TourReview.objects.create(author=request.user, body=body, num_likes=0, price=price, rating=rating, place=p)
        return redirect(request.META['HTTP_REFERER'])
    else:  
        #otherwise, generate page of all reviews for that place
        place = Place.objects.get(urlName=urlName)
        foodRev = FoodReview.objects.filter(place=place)
        stayRev = StayReview.objects.filter(place=place)
        tourRev = TourReview.objects.filter(place=place)
        return render(request, "place.html", {"place": place, "foodRev": foodRev, "stayRev" : stayRev, "tourRev": tourRev})
