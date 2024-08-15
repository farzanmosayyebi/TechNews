from rest_framework import routers

from api import views

urlpatterns = []

router = routers.DefaultRouter()

router.register("news", views.NewsViewSet, basename = "news")

urlpatterns += router.urls