from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from City.models import City, Street, Shop


class CitySerializer(ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

    def validate(self, data):
        if City.objects.filter(name=data.get('name')).exists():
            raise ValidationError({'error': 'This city already exists.'})
        return data


class StreetSerializer(ModelSerializer):
    class Meta:
        model = Street
        fields = '__all__'

    def validate(self, data):
        if Street.objects.filter(name=data.get('name'), city=data.get('city')).exists():
            raise ValidationError({'error': 'This street already exists in this city.'})
        return data


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'house', 'open_time', 'close_time', 'city', 'street']

    def validate(self, data):
        print(data)
        if Street.objects.filter(name=data.get('name'), city=data.get('city')).exists():
            raise ValidationError({'error': 'This street already exists in this city.'})
        return data
