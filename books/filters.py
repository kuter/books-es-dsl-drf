from django_filters import rest_framework as filters

from .models import Book


class NumberInFilter(filters.BaseInFilter, filters.NumberFilter):
    pass


class BookFilter(filters.FilterSet):
    id__in = NumberInFilter(field_name='id', lookup_expr='in')
    title__contains = filters.CharFilter(
        field_name='title', lookup_expr='icontains'
    )

    class Meta:
        model = Book
        fields = ('title__contains', 'id__in')
