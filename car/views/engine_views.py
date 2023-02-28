"""Module of CRUD APIViews for Engine model."""
from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

from car.filters import EngineFilter
from car.models import Engine
from car.serializers.engine_serializers import EngineSerializer


class EngineListCreateView(generics.ListCreateAPIView):
    """APIView create and list-view operations for Car model."""

    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["^engine_brand"]
    ordering_fields = ["hp", "engine_volume", "engine_brand"]
    ordering = ["engine_brand"]
    filterset_class = EngineFilter


class EngineRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """APIView retrieve, update, delete operations for Car model."""

    queryset = Engine.objects.all()
    serializer_class = EngineSerializer
