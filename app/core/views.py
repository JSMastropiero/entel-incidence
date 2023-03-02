from rest_framework import viewsets
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    SearchFilterBackend,
    DefaultOrderingFilterBackend
)
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .models import Incidence, Place, TypeOfStatus, Status, StatusChangeLog
from .documents import IncidenceDocument, PlaceDocument, StatusDocument
from .serializers import (
    IncidenceSerializer,
    PlaceSerializer,
    TypeOfStatusSerializer,
    StatusSerializer,
    StatusChangeLogSerializer,
    IncidenceDocumentSerializer,
    PlaceDocumentSerializer,
    StatusDocumentSerializer,
)


class IncidenceViewSet(viewsets.ModelViewSet):
    queryset = Incidence.objects.all()
    serializer_class = IncidenceSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = [DjangoFilterBackend, SearchFilterBackend]
    search_fields = ['place_name']


class TypeOfStatusViewSet(viewsets.ModelViewSet):
    queryset = TypeOfStatus.objects.all()
    serializer_class = TypeOfStatusSerializer


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type_of_status']


class StatusChangeLogViewSet(viewsets.ModelViewSet):
    queryset = StatusChangeLog.objects.all()
    serializer_class = StatusChangeLogSerializer


class IncidenceDocumentViewSet(DocumentViewSet):
    document = IncidenceDocument
    serializer_class = IncidenceDocumentSerializer
    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        DefaultOrderingFilterBackend
    ]
    search_fields = {
        'comment': {'boost': 4},
    }
    filter_fields = {
        'status__type_of_status__status_name': {
            'field': 'status__type_of_status__status_name.keyword',
            'lookups': ['exact', 'in', 'contains']
        },
    }
    ordering_fields = {
        'id': 'id',
    }


class PlaceDocumentViewSet(DocumentViewSet):
    document = PlaceDocument
    serializer_class = PlaceDocumentSerializer
    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        DefaultOrderingFilterBackend
    ]
    search_fields = {
        'place_name': {'boost': 4},
    }
    filter_fields = {
        'place_name': {
            'field': 'place_name.keyword',
            'lookups': ['exact', 'in', 'contains']
        },
    }
    ordering_fields = {
        'id': 'id',
    }


class StatusDocumentViewSet(DocumentViewSet):
    document = StatusDocument
    serializer_class = StatusDocumentSerializer
    filter_backends = [
        FilteringFilterBackend,
        SearchFilterBackend,
        DefaultOrderingFilterBackend
    ]
    search_fields = {
        'type_of_status__status_name': {'boost': 4},
    }
    filter_fields = {
        'type_of_status__status_name': {
            'field': 'type_of_status__status_name.keyword',
            'lookups': ['exact', 'in', 'contains']
        },
    }
    ordering_fields = {
        'id': 'id',
    }
