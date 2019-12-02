from django.shortcuts import render, redirect
from core.models import Place

# Create your views here.

def splash(request): 
    if request.method == "POST":
        name = request.POST["name"]
        Place.objects.create(name=name)
        return redirect("/")
    else: 
        places = Place.objects.all()
        return render(request, "splash.html", {"places": places})

def place(request, name):
    if request.method == "POST": 
        body = request.POST("name")
        price = request.POST("price")
        rating = request.POST("rating")
        FoodReview.objects.create(author=request.user, body=body, num_likes=0, price=price, rating=rating)
        return redirect(request.META['HTTP_REFERER'])
    else:  
        place = Place.objects.get(name=name)
        foodRev = place.food.all()
        stayRev = place.stay.all()
        tourRev = place.tour.all()
        return render(request, "place.html", {"place": place, "foodRev": foodRev, "stayRev" : stayRev, "tourRev": tourRev})
