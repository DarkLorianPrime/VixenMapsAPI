import datetime

from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from City.models import City, Street, Shop
from City.serializers import CitySerializer, StreetSerializer, ShopSerializer


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetViewSet(ModelViewSet):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    def get_queryset(self):
        return self.queryset.filter(city__id=self.kwargs.get('city_id')).all()

    def get_serializer(self, *args, **kwargs):
        if kwargs.get('data') is None:
            return self.serializer_class(*args, **kwargs)

        data = kwargs['data'].dict()
        data['city'] = self.kwargs.get('city_id')
        kwargs['data'] = data
        return self.serializer_class(*args, **kwargs)


class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get_queryset(self):
        now = datetime.datetime.now()
        params = self.request.GET.dict()
        final_query = self.queryset.filter(street_id=self.kwargs.get('street_id'), city_id=self.kwargs.get('city_id'))
        if params.get('open') is not None:
            if params.get('open') == '0':
                final_query = final_query.filter(Q(open_time__gte=now) | Q(close_time__lte=now))
            if params.get('open') == '1':
                final_query = final_query.filter(open_time__lte=now, close_time__gte=now)
        return final_query

    def get_serializer(self, *args, **kwargs):
        if kwargs.get('data') is None:
            return self.serializer_class(*args, **kwargs)
        data = kwargs['data'].dict()
        data['city'] = self.kwargs.get('city_id')
        data['street'] = self.kwargs.get('street_id')
        kwargs['data'] = data
        return self.serializer_class(*args, **kwargs)