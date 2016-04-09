from rest_framework import viewsets
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.shortcuts import get_object_or_404
from django.http import request, response
from django.shortcuts import redirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView, Response
from django.views.generic.edit import FormView
from rest_framework import generics, permissions, filters
from .models import Order
from .serializers import *
from .forms import *




class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [
        permissions.AllowAny
    ]


class RatesTableFilter(filters.FilterSet):
    class Meta:
        model = RatesTable
        fields = ['calculation_method', 'rating_id', 'carrier_service', 'fuel_surcharge', 'surcharge_other_perc',
            'surcharge_flat', 'tax_rate', 'minimum', 'break1_start', 'break1_end', 'basic1', 'kilo1', 'break2_start',
            'break2_end', 'basic2', 'kilo2', 'break3_start', 'break3_end', 'basic3', 'kilo3', 'break4_start',
            'break4_end', 'basic4', 'kilo4', 'break5_start', 'break5_end', 'basic5', 'kilo5']


class RatesTableViewSet(viewsets.ModelViewSet):
    queryset = RatesTable.objects.all()
    serializer_class = RatesTableSerializer
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



