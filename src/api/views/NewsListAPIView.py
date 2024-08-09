from rest_framework.generics import ListAPIView

from data import models
from service import serializers

class NewsListAPIView(ListAPIView):
    queryset = models.News.objects.prefetch_related("tags").all()
    serializer_class = serializers.NewsSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    