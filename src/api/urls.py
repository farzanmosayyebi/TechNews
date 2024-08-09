from django import urls
from api import views

urlpatterns = [
    urls.path("news/", views.NewsListAPIView.as_view())
]