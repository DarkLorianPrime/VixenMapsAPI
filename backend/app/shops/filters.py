from datetime import datetime

from django.db.models import QuerySet, Q, F
from django_filters import NumberFilter, CharFilter
from django_filters.rest_framework import FilterSet

from cities.models import City
from shops.models import Shop
from shops.repositories import ShopRepository

shop_repository = ShopRepository()


class ShopFilter(FilterSet):
    opened = NumberFilter(field_name="opened", method='filter_opened')
    city = CharFilter(lookup_expr="icontains", field_name="city__name")
    street = CharFilter(lookup_expr="icontains", field_name="street__name")
    house = CharFilter(lookup_expr="icontains")
    name = CharFilter(lookup_expr="icontains")

    def filter_opened(self, queryset: QuerySet, _, value):
        now = datetime.now().time()

        if value:
            is_closetime_lt_opentime = Q(close_time__lt=F('open_time'))

            filter_query = (is_closetime_lt_opentime & (Q(open_time__lte=now) | Q(close_time__gte=now)) |
                            Q(open_time__lte=now, close_time__gte=now))
        else:
            is_closetime_gt_opentime = Q(close_time__gt=F('open_time'))

            filter_query = (is_closetime_gt_opentime & (Q(open_time__gte=now) | Q(close_time__lte=now)) |
                            Q(open_time__gte=now, close_time__lte=now))

        return queryset.filter(filter_query)

    class Meta:
        model = Shop
        fields = ['opened', 'city__name', "street__name", "house", "name"]
