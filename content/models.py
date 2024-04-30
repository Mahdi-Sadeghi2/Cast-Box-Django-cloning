from django.db import models
# from django.dispatch import receiver
# from django.db.models.signals import post_save

from user_dashboard.models import Channel, CustomUser


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    mentioned_users = models.ManyToManyField(
        Channel, related_name='mentioned_in_comments', blank=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.created_at}"


class Link(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title


class Episode(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='episodes/')
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to='episode_logos/', blank=True, null=True)
    comments = models.ManyToManyField(
        Comment, related_name='episode_comments', blank=True)
    likes = models.ManyToManyField(
        CustomUser, related_name='liked_episodes', blank=True)
    links = models.ManyToManyField(
        Link, related_name='episode_links', blank=True)

    def __str__(self):
        return self.title

  


