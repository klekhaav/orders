from rest_framework import permissions, filters, viewsets
from rest_framework.authentication import TokenAuthentication
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from .serializers import *
from .forms import *


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, TokenHasReadWriteScope]


class RatesTableViewSet(viewsets.ModelViewSet):
    queryset = RatesTable.objects.all()
    serializer_class = RatesTableSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('kilo1',
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
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'state', 'country', 'postcode', 'zone')
    permission_classes = [
        permissions.AllowAny
    ]


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



