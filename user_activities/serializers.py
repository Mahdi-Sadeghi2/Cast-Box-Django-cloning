# serializers.py
from rest_framework import serializers

from .models import (Comment,
                     Like,
                     Subscription,
                     Playlist,
                     PlaylistItem,
                     WatchHistory,
                     Favorite,
                     NewEpisode)


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')
    channel_name = serializers.ReadOnlyField(source='channel.name')

    class Meta:
        model = Subscription
        fields = '__all__'


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = '__all__'


class PlaylistItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaylistItem
        fields = '__all__'


class WatchHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WatchHistory
        fields = '__all__'


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class NewEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewEpisode
        fields = '__all__'
