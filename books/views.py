from django_filters import rest_framework as filters
from rest_framework import viewsets

from .filters import BookFilter
from .models import Author, Book, Publisher, Tag
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    PublisherSerializer,
    TagSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend, )
    filterset_class = BookFilter


class PublisherViewSet(viewsets.ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
