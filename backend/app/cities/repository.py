from cities.models import City, Street


class CityRepository:
    def __init__(self):
        self.model = City

    def is_city_exists(self, name):
        return self.model.objects.filter(name=name).exists()

    def get_cities(self):
        return self.model.objects.all()

    def get_city(self, city_id):
        return self.model.objects.filter(id=city_id).first()


class StreetRepository:
    def __init__(self):
        self.model = Street

    def is_street_exists(self, city, name=None, street=None):
        query = {}
        if name:
            query = {"name": name}

        if street:
            query = {"street": street}

        return self.model.objects.filter(**query, city=city).exists()

    def get_streets(self, city_id: int):
        return self.model.objects.filter(city=city_id).all()
