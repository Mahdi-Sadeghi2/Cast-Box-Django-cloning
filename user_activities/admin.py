from django.contrib import admin
from django.contrib.admin import register


from .models import (Comment,
                     NewEpisode,Subscription,WatchHistory,Playlist,Favorite)


def make_activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


def make_deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


class BaseModelAdmin(admin.ModelAdmin):
    actions = (make_activate, make_deactivate)


@register(Comment)
class CommentAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'channel', 'created_at','text')
    list_display_links = ('id', 'channel')
    search_fields = ('channel',)


@register(NewEpisode)
class NewEpisodeAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'episode','added_at')
    list_display_links = ('id', 'episode')
    list_filter = ('episode',)
    search_fields = ('episode',)


@register(Subscription)
class SubscriptionAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'channel')
    list_display_links = ('id', 'channel')
    search_fields = ('channel',)
    

@register(WatchHistory)
class WatchHistoryAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'episode', 'watched_at')
    list_display_links = ('id', 'episode')
    search_fields = ('episode',)
    

@register(Favorite)
class FavoriteAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'episode')
    list_display_links = ('id', 'episode')
    search_fields = ('episode',)
    

@register(Playlist)
class Playlistdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)