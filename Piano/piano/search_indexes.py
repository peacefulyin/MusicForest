# coding=utf-8
from haystack import indexes
from models import Sheet


class GoodsInfoIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    album = indexes.CharField(model_attr='album')
    music = indexes.CharField(model_attr='music')

    def get_model(self):
        return Sheet

    def index_queryset(self, using=None):
        #return self.get_model().objects.values('album').distinct().order_by('album')
        return self.get_model().objects.all()