from django.contrib import admin
from django.contrib.admin import register


from .models import (Comment,
                     Episode,
                     Link)


def make_activate(modeladmin, request, queryset):
    queryset.update(is_active=True)


def make_deactivate(modeladmin, request, queryset):
    queryset.update(is_active=False)


class BaseModelAdmin(admin.ModelAdmin):
    actions = (make_activate, make_deactivate)


@register(Comment)
class CommentAdmin(BaseModelAdmin):
    list_display = ('id', 'user', 'content', 'created_at')
    list_display_links = ('id', 'content')
    search_fields = ('content',)


@register(Episode)
class ViewedContentAdmin(BaseModelAdmin):
    list_display = ('id', 'title', 'description', 'audio_file',
                    'channel', 'publish_date', 'logo')
    list_display_links = ('id', 'title', 'channel')
    list_filter = ('title', 'channel')
    search_fields = ('title',)

@register(Link)
class CommentAdmin(BaseModelAdmin):
    list_display = ('id', 'title', 'url')
    list_display_links = ('id', 'title')
    search_fields = ('title',)