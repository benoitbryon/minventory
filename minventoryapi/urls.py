"""Root URL configuration."""
from django.conf.urls import include, url

from rest_framework import routers

from minventoryapi.inventory.views import MachineViewSet
from minventoryapi.inventory.views import IPAddressViewSet


router = routers.DefaultRouter()
router.register(r'ips', IPAddressViewSet)
router.register(r'machines', MachineViewSet)

urlpatterns = [
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^', include(router.urls)),
]
