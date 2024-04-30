from rest_framework.response import Response
from rest_framework import generics, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework import generics, permissions

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import (Comment,
                     Like,
                     Playlist,
                     PlaylistItem,
                     WatchHistory,
                     Favorite,
                     NewEpisode,
                     Subscription)

from .serializers import (CommentSerializer,
                          LikeSerializer,
                          PlaylistSerializer,
                          PlaylistItemSerializer,
                          WatchHistorySerializer,
                          FavoriteSerializer,
                          NewEpisodeSerializer,
                          SubscriptionSerializer)


class CommentListCreate(generics.ListCreateAPIView, LoginRequiredMixin):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = [CommentSerializer]


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class PlaylistListCreate(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class PlaylistItemListCreate(generics.ListCreateAPIView):
    queryset = PlaylistItem.objects.all()
    serializer_class = PlaylistItemSerializer


class PlaylistItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlaylistItem.objects.all()
    serializer_class = PlaylistItemSerializer


class WatchHistoryViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = WatchHistory.objects.all()
    serializer_class = WatchHistorySerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


class NewEpisodeViewSet(viewsets.ModelViewSet):
    queryset = NewEpisode.objects.all()
    serializer_class = NewEpisodeSerializer

    def perform_create(self, serializer):

        serializer.save()

        new_episode = serializer.instance

        self.notify_subscribers(new_episode)

    def notify_subscribers(self, episode):

        channel = episode.channel

        subscribers = channel.subscribers.all()

        for subscriber in subscribers:
            NewEpisode.objects.create(user=subscriber, episode=episode)

        return Response("Notifications sent to subscribers.", status=status.HTTP_201_CREATED)


class SubscriptionViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer

