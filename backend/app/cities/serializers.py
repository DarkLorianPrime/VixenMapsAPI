from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from cities.repository import CityRepository, StreetRepository
from cities.models import City, Street

city_repository = CityRepository()
street_repository = StreetRepository()


class CitySerializer(ModelSerializer):
    name = serializers.CharField(validators=[RegexValidator(r"[а-яА-Я]{1,128}")])

    class Meta:
        model = City
        fields = ['id', "name"]

    def validate_name(self, name):
        if city_repository.is_city_exists(name=name):
            raise ValidationError('this city already exists', code=409)

        return name


class StreetSerializer(ModelSerializer):
    name = serializers.CharField()
    city = serializers.CharField(write_only=True, default=None)
    city_name = serializers.CharField(read_only=True, source="city.name")

    class Meta:
        model = Street
        fields = ['id', 'name', "city", "city_name"]

    def validate_city(self, _):
        city_id = self.context["view"].kwargs["city_id"]
        return city_repository.get_city(city_id=city_id)

    def validate(self, attrs):
        if street_repository.is_street_exists(**attrs):  # name, city
            raise ValidationError({"name": "this street in this city already exists"}, code=409)

        return attrs
