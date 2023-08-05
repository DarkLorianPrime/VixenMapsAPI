import django_filters.rest_framework
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import ModelViewSet

from cities.repository import StreetRepository, CityRepository
from cities.serializers import CitySerializer, StreetSerializer


street_repository = StreetRepository()
city_repository = CityRepository()


class CityViewSet(ModelViewSet):
    serializer_class = CitySerializer
    queryset = city_repository.get_cities()

    filterset_fields = {
        "name": ["icontains"]
    }


class StreetViewSet(ModelViewSet):
    serializer_class = StreetSerializer

    filterset_fields = {
        "name": ["icontains"]
    }

    def get_queryset(self):
        return street_repository.get_streets(city_id=self.kwargs.get("city_id"))
