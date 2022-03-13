from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Node(models.Model):
    class Meta:
        verbose_name = 'Nodes'
        verbose_name_plural = 'Nodes'
    def __str__(self):
        return self.name

    name = models.CharField(max_length=191, null=False, blank=False, verbose_name=_('Node name'))
    urlApi = models.CharField(max_length=191, null=False, blank=False, verbose_name=_('IP address'))
    nodeType = models.ForeignKey('NodeType', on_delete=models.CASCADE, verbose_name=_('Node type'), null=False, blank=False)

class NodeType(models.Model):
    class Meta:
        verbose_name = _('Node type')
        verbose_name_plural = _('Node type')
    def __str__(self):
        return self.name

    name = models.CharField(max_length=191, null=False, blank=False, verbose_name=_('Type name'))

class Socks(models.Model):
    class Meta:
        verbose_name = _('Socks')
        verbose_name_plural = _('Socks')

    def has_delete_permission(self, request, obj=None):
        return False

    ip = models.CharField(max_length=191, null=False, blank=False, verbose_name=_('socket name'))
    node = models.ForeignKey('Node', on_delete=models.CASCADE, verbose_name=_('Node type'))
