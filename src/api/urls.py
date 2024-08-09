from django import urls
from rest_framework import routers
from api import views


urlpatterns = [
    urls.path("news/", views.NewsListAPIView.as_view())
]