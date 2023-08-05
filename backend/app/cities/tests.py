from django.test import TestCase

from cities.models import City, Street


class CitiesTestCase(TestCase):
    def setUp(self):
        self._id = City.objects.create(name="Москва").id
        self._id1 = City.objects.create(name="Питер").id
        Street.objects.create(city_id=self._id1, name="Нелюбимая")

    def test_cities_created_successful(self):
        result = self.client.post("http://127.0.0.1:8000/api/v1/city/", data={"name": "Ульяновск"})
        self.assertEquals(result.status_code, 201)
        self.assertEquals(result.json()["name"], "Ульяновск")

    def test_cities_already_exists(self):
        result = self.client.post("http://127.0.0.1:8000/api/v1/city/", data={"name": "Питер"})
        self.assertEquals(result.status_code, 400)

    def test_create_street_successful(self):
        result = self.client.post(f"http://127.0.0.1:8000/api/v1/city/{self._id1}/street/", data={"name": "Любимая"})
        self.assertEquals(result.status_code, 201)
        self.assertEquals(result.json()["name"], "Любимая")

    def test_create_street_already_exists(self):
        result = self.client.post(f"http://127.0.0.1:8000/api/v1/city/{self._id1}/street/", data={"name": "Нелюбимая"})
        self.assertEquals(result.status_code, 400)

    def test_create_street_successful_other(self):
        result = self.client.post(f"http://127.0.0.1:8000/api/v1/city/{self._id}/street/", data={"name": "Нелюбимая"})
        self.assertEquals(result.status_code, 201)
        self.assertEquals(result.json()["name"], "Нелюбимая")
