from django.contrib import admin
from core.models import Place
from core.models import FoodReview, StayReview, TourReview


# Register your models here.

admin.site.register(Place)
admin.site.register(FoodReview)
admin.site.register(StayReview)
admin.site.register(TourReview)