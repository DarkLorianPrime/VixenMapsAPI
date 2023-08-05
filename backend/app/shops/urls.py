from django.urls import path

from shops.views import ShopViewSet

urlpatterns = [
    path('', ShopViewSet.as_view({"get": "list", "post": "create"}), name="control shops")
]