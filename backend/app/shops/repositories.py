from shops.models import Shop


class ShopRepository:
    def __init__(self):
        self.model = Shop

    def get_all_shops(self):
        return self.model.objects.all()

    def is_shop_exists(self, city, street, house, name, **_):
        return self.model.objects.filter(city=city, street=street, house=house, name=name).exists()

    def is_shop_opened(self, close_time, open_time, current_time):
        return ((close_time < open_time and (open_time <= current_time or close_time >= current_time))
                or (open_time <= current_time <= close_time))
