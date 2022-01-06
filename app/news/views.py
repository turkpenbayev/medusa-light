from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, mixins
from rest_framework.filters import OrderingFilter, SearchFilter

from .models import New
from .serializers import NewsReadSerializer
from utils.views import ActionSerializerViewSetMixin


class NewsViewSet(
    ActionSerializerViewSetMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['subject']
    ordering_fields = ['date']
    filterset_fields = ['date']
    serializer_classes = {
        'list': NewsReadSerializer,
    }
    queryset = New.objects.order_by('-date')
