from rest_framework import serializers
from .models import Episode, Comment, Link


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    user_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'
