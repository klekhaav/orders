from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'rate', views.RateViewSet)
router.register(r'rates_table', views.RatesTableViewSet)
router.register(r'locality', views.LocalityViewSet)
router.register(r'carrier_service', views.CarrierServiceViewSet)
router.register(r'rating_id', views.RatingIdViewSet)
router.register(r'order', views.OrderViewSet)
#router.register(r'order/(?P<pk>[0-9]+)/$', views.OrderDetail, base_name='detail')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]