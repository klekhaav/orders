from rest_framework import permissions, filters, viewsets
from .serializers import *
from .forms import *


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class RatesTableViewSet(viewsets.ModelViewSet):
    queryset = RatesTable.objects.all()
    serializer_class = RatesTableSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = (
        'rating_id__rating_id',
        'carrier_service__title',
        'carrier_service__service',
        'carrier_service__zone_from',
        'carrier_service__zone_from_postcode',
        'carrier_service__zone_to',
        'carrier_service__zone_to_postcode')
    permission_classes = [
        permissions.AllowAny
    ]


class LocalityViewSet(viewsets.ModelViewSet):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer


class CarrierServiceViewSet(viewsets.ModelViewSet):
    queryset = CarrierService.objects.all()
    serializer_class = CarrierServiceSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class RatingIdViewSet(viewsets.ModelViewSet):
    queryset = RatingId.objects.all()
    serializer_class = RatingIdSerializer



