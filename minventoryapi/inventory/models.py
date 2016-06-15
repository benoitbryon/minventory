from django.db import models
from django.utils.translation import ugettext_lazy as _

from rest_framework.reverse import reverse
from uuidfield import UUIDField


class Machine(models.Model):
    """A machine in IT architecture."""
    created_on = models.DateTimeField(
        verbose_name=_('created on'),
        auto_now_add=True,
    )
    configuration = models.TextField(
        verbose_name=_('configuration'),
        blank=True,
    )
    customer = models.CharField(
        verbose_name=_('customer'),
        max_length=30,
        db_index=True,
    )
    environment = models.CharField(
        verbose_name=_('environment'),
        max_length=20,
        db_index=True,
    )
    group = models.CharField(
        verbose_name=_('group'),
        max_length=30,
        db_index=True,
        blank=True,
    )
    last_modified_on = models.DateTimeField(
        verbose_name=_('last modified on'),
        auto_now=True,
    )
    location = models.CharField(
        verbose_name=_('location'),
        max_length=200,
        blank=True,
    )
    machine_lifecycle = models.CharField(
        verbose_name=_('lifecycle'),
        max_length=20,
        db_index=True,
        choices=[
            ('nonexistent', _('nonexistent')),
            ('creating', _('hosting service provider creates machine')),
            ('created', _('empty machine created')),
            ('installing', _('OS being installed')),
            ('installed', _('OS installed')),
            ('provisioning', _('provisioning')),
            ('provisioned', _('provisioned')),
            ('removing', _('machine being removed')),
            ('removed', _('machine removed')),
        ]
    )
    machine_name = models.CharField(
        verbose_name=_('machine name'),
        max_length=100,
        unique=True,
    )
    machine_product = models.CharField(
        verbose_name=_('machine product'),
        max_length=100,
        blank=True,
        help_text=_('Commercial product model, from hosting.'),
    )
    machine_type = models.CharField(
        verbose_name=_('type'),
        max_length=20,
        db_index=True,
        choices=[
            ('vm', _('virtual machine')),
            ('physical', _('physical machine')),
        ]
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
        unique=True,
    )
    os = models.CharField(
        verbose_name=_('OS'),
        max_length=50,
        blank=True,
        help_text=_('Operating system.'),
    )
    role = models.CharField(
        verbose_name=_('role'),
        max_length=30,
    )
    state = models.CharField(
        verbose_name=_('state'),
        max_length=20,
        db_index=True,
        choices=[
            ('unavailable', _('nonexistent')),
            ('normal', _('normal')),
            ('warning', _('warning')),
            ('error', _('error')),
        ]
    )
    uuid = UUIDField(
        auto=True,
        hyphenate=False,
    )

    class Meta:
        ordering = ('customer', 'environment', 'group', 'role', 'name')

    def __unicode__(self):
        return u'{}/{}/{}/{} - {}'.format(
            self.customer,
            self.environment,
            self.group,
            self.role,
            self.name)

    def get_absolute_url(self, **kwargs):
        return reverse('machine-detail', args=[self.uuid], **kwargs)


class IPAddress(models.Model):
    """An IP address."""
    created_on = models.DateTimeField(
        verbose_name=_('created on'),
        auto_now_add=True,
    )
    ip = models.GenericIPAddressField(
        verbose_name=_('IP'),
        primary_key=True,
    )
    is_physical = models.BooleanField(
        verbose_name=_('is physical'),
        default=False,
        db_index=True,
        help_text=_('True if IP is tied to hardware ; False if failover type'),
    )
    last_modified_on = models.DateTimeField(
        verbose_name=_('last modified on'),
        auto_now=True,
    )
    machine = models.ForeignKey(
        Machine,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='ips',
    )

    class Meta:
        ordering = ('ip', 'is_physical')

    def __unicode__(self):
        return self.ip

    def get_absolute_url(self, **kwargs):
        return reverse('ipaddress-detail', args=[self.ip], **kwargs)
