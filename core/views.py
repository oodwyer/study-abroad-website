from django.shortcuts import render, redirect
from core.models import Place, FoodReview, StayReview, TourReview
from whoosh.fields import Schema, STORED, ID, KEYWORD, TEXT 
import os.path 
from whoosh.index import create_in 
from haystack.query import SearchQuerySet

# Create your views here.
""" def search(request): 
    if request.method == "GET":
        #food_reviews = FoodReview.objects.get(body=request.POST.get('search_text', ''))
        print(request.POST.get('search_text'))
        food_reviews = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text'))
        for f in food_reviews: 
            print("test")
            print(f.body)
        return render(request, "search/search.html", {'food_reviews': food_reviews})
    else: 
        food_reviews = set()
        return render(request, "search/search.html", {'food_reviews': food_reviews})

def search_titles(request):
    food_reviews = SearchQuerySet().autocomplete(content_auto=request.POST.get('search_text', ''))
    return render(request, "search.html", {'food_reviews': food_reviews})
 """

#main page 
def splash(request): 
    if request.method == "POST":
        name = request.POST["name"]
        Place.objects.create(name=name)
        return redirect("/")
    else: 
        places = Place.objects.all()
        return render(request, "splash.html", {"places": places})

#place specific page
def place(request, name):
    if request.method == "POST": 
        body = request.POST["name"]
        price = request.POST["price"]
        rating = request.POST["rating"]

        p = Place.objects.get(name=name)

        #which type of review? check which button 
        if 'food' in request.POST:
            f = FoodReview.objects.create(author=request.user, body=body, num_likes=0, price=price, rating=rating, place=p)
            #p.food.add(f)
        elif 'stay' in request.POST: 
            s = StayReview.objects.create(author=request.user, body=body, num_likes=0, price=price, rating=rating, place=p)
            #p.stay.add(s)
        elif 'tour' in request.POST: 
            t = TourReview.objects.create(author=request.user, body=body, num_likes=0, price=price, rating=rating, place=p)
            #p.tour.add(t)
        return redirect(request.META['HTTP_REFERER'])
    else:  
        place = Place.objects.get(name=name)
        #foodRev = place.food.all()
        foodRev = FoodReview.objects.filter(place=place)
        stayRev = StayReview.objects.filter(place=place)
        tourRev = TourReview.objects.filter(place=place)
        return render(request, "place.html", {"place": place, "foodRev": foodRev, "stayRev" : stayRev, "tourRev": tourRev})
