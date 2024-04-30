from rest_framework import serializers

from .models import (Channel,
                     ChannelHistory,
                     ChannelFavorite,
                     NewEpisode,
                     CustomUser,
                     Subscriptions)


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

    def get_subscribers(self, obj):
        return obj.get_subscriber_members().values_list('id', flat=True)


class ChannelHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelHistory
        fields = '__all__'


class ChannelFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelFavorite
        fields = '__all__'


class NewEpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewEpisode
        fields = '__all__'


class SubscriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriptions
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'gender']
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user = CustomUser(
    #         username=validated_data['username'],
    #         email=validated_data['email']
    #     )
    #     user.set_password(validated_data['password'])
    #     user.save()
    #     return user
