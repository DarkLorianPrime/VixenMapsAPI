from django.test import TestCase

from cities.models import City, Street


class ShopTestCase(TestCase):
    def setUp(self):
        self._id = City.objects.create(name="Москва").id
        self._id1 = City.objects.create(name="Питер").id
        self.street = Street.objects.create(city_id=self._id, name="Любимая").id
        self.street1 = Street.objects.create(city_id=self._id1, name="Нелюбимая").id
        self.client.post("http://127.0.0.1:8000/api/v1/shop/", data={"name": "VixenSoft",
                                                                     "house": "1234",
                                                                     "city": self._id,
                                                                     "street": self.street,
                                                                     "open_time": "12:00",
                                                                     "close_time": "10:00"})

    def test_create_shop_successful(self):
        result = self.client.post("http://127.0.0.1:8000/api/v1/shop/", data={"name": "VixenSoft",
                                                                              "house": "123",
                                                                              "city": self._id,
                                                                              "street": self.street,
                                                                              "open_time": "12:00",
                                                                              "close_time": "10:00"})
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json()["name"], "VixenSoft")

    def test_create_shop_already_exists(self):
        result = self.client.post("http://127.0.0.1:8000/api/v1/shop/", data={"name": "VixenSoft",
                                                                              "house": "1234",
                                                                              "city": self._id,
                                                                              "street": self.street,
                                                                              "open_time": "12:00",
                                                                              "close_time": "10:00"})
        self.assertEqual(result.status_code, 400)

    def test_create_shop_other_street(self):
        result = self.client.post("http://127.0.0.1:8000/api/v1/shop/", data={"name": "VixenSoft",
                                                                              "house": "123",
                                                                              "city": self._id1,
                                                                              "street": self.street1,
                                                                              "open_time": "12:00",
                                                                              "close_time": "10:00"})
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json()["name"], "VixenSoft")

    def test_create_shop_street_nf(self):
        result = self.client.post("http://127.0.0.1:8000/api/v1/shop/", data={"name": "VixenSoft",
                                                                              "house": "123",
                                                                              "city": self._id,
                                                                              "street": self.street1,
                                                                              "open_time": "12:00",
                                                                              "close_time": "10:00"})
        self.assertEqual(result.status_code, 400)
