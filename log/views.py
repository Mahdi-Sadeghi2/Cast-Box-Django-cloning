from rest_framework import generics
from .models import ViewedContent, ViewedChannel
from .serializers import ViewedContentSerializer, ViewedChannelSerializer


class ViewedContentListCreate(generics.ListCreateAPIView):
    queryset = ViewedContent.objects.all()
    serializer_class = ViewedContentSerializer

class ViewedContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ViewedContent.objects.all()
    serializer_class = ViewedContentSerializer

class ViewedChannelListCreate(generics.ListCreateAPIView):
    queryset = ViewedChannel.objects.all()
    serializer_class = ViewedChannelSerializer

class ViewedChannelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ViewedChannel.objects.all()
    serializer_class = ViewedChannelSerializer
