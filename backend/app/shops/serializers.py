from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer

from cities.repository import CityRepository, StreetRepository
from shops.models import Shop
from shops.repositories import ShopRepository

shop_repository = ShopRepository()
city_repository = CityRepository()
street_repository = StreetRepository()


class ShopSerializer(ModelSerializer):
    name = serializers.CharField(validators=[RegexValidator(r"[а-яА-Я,-_ ]{1,128}")])
    city_name = serializers.CharField(read_only=True, source="city.name")
    street_name = serializers.CharField(read_only=True, source="street.name")

    class Meta:
        model = Shop
        extra_kwargs = {"city": {"write_only": True},
                        "street": {"write_only": True}}
        fields = '__all__'

    def validate_city(self, city):
        return city

    def validate_street(self, street):
        if street.city.id != int(self.context["city"]):
            raise ValidationError("this street in this city not exists", 404)

        return street

    def validate(self, attrs):
        if shop_repository.is_shop_exists(**attrs):
            raise ValidationError({"name": "this shopname already exists in this house"}, 400)

        return attrs




