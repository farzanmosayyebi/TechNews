from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from data import models
from service import pagination, serializers

tag_param = openapi.Parameter("tags",
                            openapi.IN_QUERY,
                            type = openapi.TYPE_ARRAY,
                            items = openapi.Items(type = "string"),
                            description = "Filter by tag.")

class NewsViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = models.News.objects.prefetch_related("tags").all()
    serializer_class = serializers.NewsSerializer
    pagination_class = pagination.CustomPagiation

    @swagger_auto_schema(manual_parameters = [tag_param])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        tag_titles = request.GET.get("tags")
        if tag_titles is not None:
            tag_titles = tag_titles.strip().split(",")
            tags = models.Tag.objects.filter(title__in=tag_titles)
            queryset = queryset.filter(tags__in=tags).distinct()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    