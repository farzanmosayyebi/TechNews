from django import urls
from rest_framework import routers
from api import views


urlpatterns = [
    urls.path("news/", views.NewsListView.as_view())
]