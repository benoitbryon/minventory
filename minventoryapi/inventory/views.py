from rest_framework import filters
from rest_framework import viewsets

from minventoryapi.inventory import models
from minventoryapi.inventory import serializers


class MachineFilterSet(filters.FilterSet):
    class Meta:
        model = models.Machine
        fields = {
            'name': ['icontains'],
            'location': ['icontains'],
            'uuid': ['exact'],
        }


class MachineViewSet(viewsets.ModelViewSet):
    filter_class = MachineFilterSet
    lookup_field = 'uuid'
    lookup_value_regex = '[0-9a-f]{32}'
    queryset = models.Machine.objects.all()
    serializer_class = serializers.MachineSerializer


class IPAddressFilterSet(filters.FilterSet):
    class Meta:
        model = models.IPAddress
        fields = {
            'ip': ['icontains'],
        }


class IPAddressViewSet(viewsets.ModelViewSet):
    filter_class = IPAddressFilterSet
    lookup_field = 'ip'
    lookup_value_regex = '[0-9a-f.:-]{7,45}'
    queryset = models.IPAddress.objects.all()
    serializer_class = serializers.IPAddressSerializer
