from django.urls import path
from rest_framework.routers import SimpleRouter

from City.views import CityViewSet, StreetViewSet, ShopViewSet

urlpatterns = [
    path('city/', CityViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('city/<int:city_id>/street/', StreetViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('city/<int:city_id>/street/<int:street_id>/shop/', ShopViewSet.as_view({'get': 'list', 'post': 'create'}))
]
