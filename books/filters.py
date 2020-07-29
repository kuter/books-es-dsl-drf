from django_filters import rest_framework as filters

from .models import Book


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class BookFilter(filters.FilterSet):
    id__in = NumberInFilter(field_name="id", lookup_expr='in')

    class Meta:
        model = Book
        fields = ('price', 'id__in')
