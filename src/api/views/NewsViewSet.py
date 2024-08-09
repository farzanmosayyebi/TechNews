from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from data import models
from service import serializers
from service import pagination

tag_param = openapi.Parameter("tags",
                            openapi.IN_QUERY,
                            type = openapi.TYPE_STRING,
                            description = "Filter by tags. values must be separated by ',' (e.g. Technology,Programming)")

class NewsViewSet(mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = models.News.objects.prefetch_related("tags").all()
    serializer_class = serializers.NewsSerializer
    pagination_class = pagination.CustomPagiation

    @swagger_auto_schema(manual_parameters = [tag_param])
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        tags = request.GET.get("tags")
        if tags is not None:
            tags = tags.strip().split(",")
            tag_list = models.Tag.objects.filter(title__in = tags)
            queryset = queryset.filter(tags__in = tag_list).distinct()

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    