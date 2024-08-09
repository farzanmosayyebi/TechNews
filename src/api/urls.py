from django import urls
from api import views
from rest_framework import routers

urlpatterns = [
    # urls.path("news/", views.NewsListAPIView)
]

router = routers.DefaultRouter()

router.register("news", views.NewsViewSet, basename = "news")

urlpatterns += router.urls