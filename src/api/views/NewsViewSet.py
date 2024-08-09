from django_filters import rest_framework as filters
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import mixins, viewsets
from rest_framework.response import Response

from data import models
from service import filters as appfilters
from service import pagination, serializers

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
    filter_backends = [
        filters.DjangoFilterBackend,
    ]
    filterset_class = appfilters.NewsFilter

    @swagger_auto_schema(manual_parameters = [tag_param])
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        filter = appfilters.NewsFilter(data = request.GET, queryset = queryset)
        queryset = filter.qs

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    