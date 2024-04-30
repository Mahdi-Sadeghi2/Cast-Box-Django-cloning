from django.contrib import admin
from django.contrib.admin import register


from .models import (ViewedContent,
                     ViewedChannel)


def make_activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


def make_deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


class BaseModelAdmin(admin.ModelAdmin):
    actions = (make_activate, make_deactivate)


@register(ViewedChannel)
class ViewedChannelAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'channel', 'viewed_at')
    list_display_links = ('id', 'channel')
    search_fields = ('channel',)


@register(ViewedContent)
class ViewedContentAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'episode',
                    'viewed_at')
    list_display_links = ('id', 'episode')
    list_filter = ('episode',)
    search_fields = ('episode',)


