from django.contrib import admin
from django.contrib.admin import register


from .models import (ChannelHistory,
                     NewEpisode, ChannelFavorite, Channel, CustomUser)


def make_activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


def make_deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


class BaseModelAdmin(admin.ModelAdmin):
    actions = (make_activate, make_deactivate)


@register(Channel)
class ChannelAdmin(BaseModelAdmin):
    list_display = ('id', 'owner', 'name', 'description', 'is_public', 'is_active', 'host', 'language',
                    'genre', 'duration', 'creation_date', 'episode_count', 'release_schedule', 'logo')
    list_display_links = ('id', 'name', 'owner')
    search_fields = ('name', 'owner')


@register(ChannelHistory)
class ChannelHistoryAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'channel', 'last_watched')
    list_display_links = ('id', 'channel')
    search_fields = ('channel',)


@register(ChannelFavorite)
class ChannelFavoriteAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'channel')
    list_display_links = ('id', 'channel')
    list_filter = ('channel',)
    search_fields = ('channel',)


@register(NewEpisode)
class NewEpisodeAdmin(BaseModelAdmin):
    list_display = ('id', 'episode_count', 'channel', 'last_updated')
    list_display_links = ('id', 'channel')
    search_fields = ('channel', 'episode_count')


@register(CustomUser)
class UserAdmin(BaseModelAdmin):
    list_display = ('id', 'email', 'username',)
    # list_display_links = ('id', 'name')
    # search_fields = ('name', 'owner')
