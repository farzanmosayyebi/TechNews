from django_filters import rest_framework
from data import models

class NewsFilter(rest_framework.FilterSet):
    tags = rest_framework.CharFilter(field_name = "tags__title", lookup_expr = "icontains")

    class Meta:
        model = models.News
        fields = [
            "tags",
        ]