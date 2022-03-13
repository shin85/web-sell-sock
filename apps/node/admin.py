# from multiprocessing.dummy import active_children
from django.contrib import admin
from django import forms
from .models import Node, NodeType, Socks
from django.utils.translation import gettext_lazy as _
from django.utils.translation import activate, get_language, get_language_info

@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'urlApi', 'nodeType')

# @admin.register(NodeType)
# class NodeTypeAdmin(admin.ModelAdmin):
#     list_display = ('name',)

@admin.register(Socks)
class SocksAdmin(admin.ModelAdmin):
    list_display = ('ip', 'node')
