import factory
import datetime

from factory.fuzzy import FuzzyDate, FuzzyDecimal, FuzzyChoice

from .models import Book, Publisher, BOOK_PUBLISHING_STATUS_CHOICES


class PublisherFactory(factory.DjangoModelFactory):

    name = factory.Faker('name')

    class Meta:
        model = Publisher


class BookFactory(factory.DjangoModelFactory):

    title = factory.Faker('sentence', nb_words=4)
    publisher = factory.SubFactory(PublisherFactory)
    publication_date = FuzzyDate(datetime.date(2020, 1, 1))
    price = FuzzyDecimal(10, 100, 2)
    isbn = factory.Faker('isbn13')
    state = FuzzyChoice(dict(BOOK_PUBLISHING_STATUS_CHOICES).keys())

    class Meta:
        model = Book
