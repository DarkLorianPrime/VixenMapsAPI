from django.db import models


class City(models.Model):
    name = models.CharField()

    class Meta:
        ordering = ["-id"]


class Street(models.Model):
    name = models.CharField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-id"]