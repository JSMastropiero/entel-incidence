from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

from .models import Incidence, Place, TypeOfStatus, Status, StatusChangeLog
from .documents import IncidenceDocument, PlaceDocument, StatusDocument


class IncidenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incidence
        fields = '__all__'


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'


class TypeOfStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfStatus
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    type_of_status = TypeOfStatusSerializer()

    class Meta:
        model = Status
        fields = '__all__'


class StatusChangeLogSerializer(serializers.ModelSerializer):
    status = StatusSerializer()

    class Meta:
        model = StatusChangeLog
        fields = '__all__'


class IncidenceDocumentSerializer(DocumentSerializer):
    class Meta(object):
        document = IncidenceDocument


class PlaceDocumentSerializer(DocumentSerializer):
    class Meta(object):
        document = PlaceDocument


class StatusDocumentSerializer(DocumentSerializer):
    class Meta(object):
        document = StatusDocument
