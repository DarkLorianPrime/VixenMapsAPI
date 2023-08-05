from django.db import models


class Shop(models.Model):
    name = models.CharField()
    house = models.CharField()
    street = models.ForeignKey("cities.Street", on_delete=models.CASCADE)
    city = models.ForeignKey("cities.City", on_delete=models.CASCADE)
    open_time = models.TimeField()
    close_time = models.TimeField()

    class Meta:
        ordering = ["-id"]