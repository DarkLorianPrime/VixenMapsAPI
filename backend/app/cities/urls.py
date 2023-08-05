from django.urls import path, include

from cities.views import CityViewSet, StreetViewSet

urlpatterns = [
    path('', CityViewSet.as_view({"get": "list", "post": "create"}), name="control cities"),
    path('<int:city_id>/street/', StreetViewSet.as_view({"get": "list", "post": "create"}), name="control streets")

]
