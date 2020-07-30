from django_filters import rest_framework as filters
from rest_framework import viewsets

from .filters import BookFilter
from .models import Book, Publisher
from .serializers import BookSerializer, PublisherSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = BookFilter


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
