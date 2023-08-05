from rest_framework.viewsets import ModelViewSet

from shops.filters import ShopFilter
from shops.repositories import ShopRepository
from shops.serializers import ShopSerializer

shop_repository = ShopRepository()


class ShopViewSet(ModelViewSet):
    queryset = shop_repository.get_all_shops()
    serializer_class = ShopSerializer
    filterset_class = ShopFilter

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"city": self.request.data.get("city")})
        return context
