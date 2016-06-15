from rest_framework import serializers

from minventoryapi.inventory import models


class IPAddressSerializer(serializers.HyperlinkedModelSerializer):
    ip = serializers.IPAddressField()

    class Meta:
        model = models.IPAddress
        fields = (
            'created_on',
            'ip',
            'is_physical',
            'last_modified_on',
            'machine',
            'url',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'ip'},
            'machine': {'lookup_field': 'uuid'},
        }


class MachineSerializer(serializers.HyperlinkedModelSerializer):
    ips = IPAddressSerializer(many=True, read_only=True)
    uuid = serializers.UUIDField(format='hex', read_only=True)

    class Meta:
        model = models.Machine
        fields = (
            'uuid',
            'created_on',
            'configuration',
            'customer',
            'environment',
            'group',
            'ips',
            'location',
            'last_modified_on',
            'machine_lifecycle',
            'machine_name',
            'machine_product',
            'machine_type',
            'name',
            'os',
            'role',
            'state',
            'url',
        )
        extra_kwargs = {
            'url': {'lookup_field': 'uuid'},
        }
