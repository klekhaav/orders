from django.conf.urls import url, include
from rest_framework import routers
from .views import *
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'rate', RateViewSet)
router.register(r'rates_table', RatesTableViewSet)
router.register(r'locality', LocalityViewSet)
router.register(r'carrier_service', CarrierServiceViewSet)
router.register(r'rating_id', RatingIdViewSet)
router.register(r'order', OrderViewSet)

#router.register(r'order/(?P<pk>[0-9]+)/$', OrderDetail, base_name='detail')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', include(admin.site.urls)),
]