from rest_framework import generics, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token


from django.contrib.auth import authenticate


from .models import (Channel,
                     Subscriptions,
                     ChannelFavorite,
                     ChannelHistory,
                     NewEpisode)

from .serializers import (UserSerializer,
                          ChannelSerializer,
                          ChannelFavoriteSerializer,
                          ChannelHistorySerializer,
                          NewEpisodeSerializer,
                          SubscriptionsSerializer)


@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)


class ChannelListCreate(generics.ListCreateAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


class ChannelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        channel = self.get_object()
        subscribers = channel.get_subscriber_members()
        serializer = UserSerializer(subscribers, many=True)
        response.data['subscribers'] = serializer.data
        return response

class WatchHistoryViewSet(viewsets.ModelViewSet):
    queryset = ChannelHistory.objects.all()
    serializer_class = ChannelHistorySerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    queryset = ChannelFavorite.objects.all()
    serializer_class = ChannelFavoriteSerializer


class NewEpisodeViewSet(viewsets.ModelViewSet):
    queryset = NewEpisode.objects.all()
    serializer_class = NewEpisodeSerializer
