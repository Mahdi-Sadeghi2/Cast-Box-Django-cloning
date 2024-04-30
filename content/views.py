from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from django.http import FileResponse



from .models import Episode, Comment, Link, Channel

from .serializers import EpisodeSerializer, CommentSerializer, LinkSerializer


class CommentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        for channel_data in data:
            channel_id = channel_data['id']
            channel = Channel.objects.get(id=channel_id)
            channel_data['episode_count'] = channel.episode_count
        return Response(data)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LinkListCreateAPIView(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LinkDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class EpisodeListCreate(generics.ListCreateAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer


class EpisodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
    
    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        episode = self.get_object()
        if not request.user.is_authenticated:
            return Response({'error': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
        
        if episode.audio_file:
            audio_file_path = episode.audio_file.path
            response = FileResponse(open(audio_file_path, 'rb'), as_attachment=True)
            return response
        else:
            return Response({'error': 'No audio file attached to this episode.'}, status=status.HTTP_404_NOT_FOUND)

    def get_permissions(self):
        if self.action == 'download':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]