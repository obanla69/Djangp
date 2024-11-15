from django_filters import FilterSet
from .models import Products


class ProductsFilter(FilterSet):
    class Meta:
        model = Products
        fields = {
            'title': ['exact'],
            'price': ['gt', 'lt'],
        }
