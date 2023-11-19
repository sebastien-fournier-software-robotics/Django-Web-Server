from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from part1.views import UrlViewSet
from part2.views import ExchangeDataViewSet

router = routers.SimpleRouter()

router.register("url", UrlViewSet, basename="url")
router.register("exchangedata", ExchangeDataViewSet, basename="exchangedata")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/", include(router.urls)),
]
