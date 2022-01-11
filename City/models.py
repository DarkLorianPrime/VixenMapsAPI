from django.db import models


class City(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Street(models.Model):
    name = models.CharField(max_length=250)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='City_Street')

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=250)
    city = models.ForeignKey('City', on_delete=models.CASCADE, related_name='City_Shop')
    street = models.ForeignKey('Street', on_delete=models.CASCADE, related_name='Street_Shop')
    house = models.CharField(max_length=10)
    open_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return self.name

