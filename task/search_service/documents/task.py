from django.conf import settings
from django_elasticsearch_dsl import Document, Index, fields
from elasticsearch_dsl import analyzer

from task.api.models import Task

# Name of the Elasticsearch index
INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES[__name__])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = analyzer(
    'html_strip',
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"]
)

@INDEX.doc_type
class TaskDocument(Document):
    """Task Elasticsearch document."""

    id = fields.IntegerField(attr='id')

    name = fields.TextField(
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', fielddata=True),
        },
    )

    created_by = fields.TextField(
        attr='created_by_indexing',
        analyzer=html_strip,
        fields={
            'raw': fields.TextField(analyzer='keyword', fielddata=True),
        },
    )
    
    
    class Django(object):
        """Inner nested class Django.""" 

        model = Task  # The model associate with this DocType