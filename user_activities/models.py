from django.db import models
from content.models import Episode
from user_dashboard.models import Channel, CustomUser


class Comment(models.Model):
    user = models.ForeignKey(
        CustomUser, related_name='user_activities_comments', on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def delete_comment(self):
        self.delete()


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'episode')

    def unlike_episode(self):
        self.delete()


class Subscription(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)


class Playlist(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    podcasts = models.ForeignKey(Channel, on_delete=models.CASCADE, null=True)

    def delete_playlist(self):
        self.delete()


class PlaylistItem(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)


class WatchHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    watched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'episode')

    def unlisten_content(self):
        self.delete()


class Favorite(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'episode')


class NewEpisode(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
