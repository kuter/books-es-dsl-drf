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

html_strip = analyzer(
    'html_strip',
    tokenizer='standard',
    # filter=['lowercase', 'stop', 'snowball'],
    # char_filter=['html_strip']
)


@INDEX.doc_type
class BookDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    title = fields.KeywordField(
        #analyzer=html_strip,
        # fields={
        #     'raw': fields.KeywordField(analyzer='keyword'),
        # }
    )

    description = fields.KeywordField(
        #analyzer=html_strip,
        # fields={
        #     'raw': fields.KeywordField(analyzer='keyword'),
        # }
    )

    summary = fields.KeywordField(
        #analyzer=html_strip,
        # fields={
        #     'raw': fields.KeywordField(analyzer='keyword'),
        # }
    )

    publisher = fields.KeywordField(
        attr='publisher_indexing',
        #analyzer=html_strip,
        # fields={
        #     'raw': fields.KeywordField(analyzer='keyword'),
        # }
    )

    publication_date = fields.DateField()

    state = fields.KeywordField(
        #analyzer=html_strip,
        # fields={
        #     'raw': fields.KeywordField(analyzer='keyword'),
        # }
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
