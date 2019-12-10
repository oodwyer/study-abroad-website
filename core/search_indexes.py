import datetime
from haystack import indexes
from core.models import FoodReview

class FoodReviewIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    created_at = indexes.DateTimeField(model_attr='created_at')
    author = indexes.CharField(model_attr='author')
    #content_auto = indexes.EdgeNgramField(model_attr='body')

    def get_model(self):
        return FoodReview
    
    def index_queryset(self, using=None):
        #used when entire index for model is updated 
        return self.get_model().objects.all()

