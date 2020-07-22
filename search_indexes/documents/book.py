from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from books.models import Book

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])


# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1,
)


@INDEX.doc_type
class BookDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')
    title = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
        }
    )
    description = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
        }
    )

    summary = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
        }
    )

    publisher = fields.KeywordField(
        attr='publisher_indexing',
        #analyzer=html_strip,
        # fields={
        #     'raw': fields.KeywordField(analyzer='keyword'),
        # }
    )

    publication_date = fields.DateField()

    state = fields.TextField(
        fields={
            'raw': fields.KeywordField(),
        }
    )

    isbn = fields.KeywordField(
        #analyzer=html_strip,
        # fields={
        #     'raw': fields.KeywordField(analyzer='keyword'),
        # }
    )

    price = fields.FloatField()

    pages = fields.IntegerField()

    stock_count = fields.IntegerField()

    tags = fields.KeywordField(
        attr='tags_indexing',
        #analyzer=html_strip,
        # fields={
        #     'raw': fields.KeywordField(analyzer='keyword', multi=True),
        #     'suggest': fields.CompletionField(multi=True),
        # },
        multi=True
    )

    class Django(object):
        """Inner nested class Django."""

        model = Book  # The model associate with this Document
