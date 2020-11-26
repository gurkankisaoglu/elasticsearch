import json

from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .documents.task import TaskDocument

class TaskDocumentSerializer(DocumentSerializer):
    """Serializer for the Task document."""

    class Meta(object):
        """Meta options."""

        # Specify the correspondent document class
        document = TaskDocument

        # List the serializer fields. Note, that the order of the fields
        # is preserved in the ViewSet.
        fields = (
            'id',
            'name',
            'created_by',
        )