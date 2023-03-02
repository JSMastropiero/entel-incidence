from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Incidence, Place, Status

@registry.register_document
class IncidenceDocument(Document):
    place_name = fields.TextField(attr='place.place_name')
    status_name = fields.TextField(attr='status.type_of_status.status_name')

    class Index:
        name = 'incidences'
        settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Incidence
        fields = ['comment']

