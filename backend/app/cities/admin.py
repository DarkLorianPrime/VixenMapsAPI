from django.contrib import admin

from cities import models

admin.register(models.City, models.Street)
