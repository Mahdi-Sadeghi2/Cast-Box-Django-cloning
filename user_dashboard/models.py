from django.contrib.auth.models import AbstractUser
from django.db import models



class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)

    def __str__(self):
        return self.username




class Channel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    host = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    duration = models.DurationField()
    episode_count = models.IntegerField(default=0)
    release_schedule = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='channel_logos/', blank=True, null=True)

    
    def get_subscriber_members(self):
        return self.members.filter(subscriptions__channel=self).distinct()
    
    def __str__(self):
        return self.name
    


class ChannelHistory(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    last_watched = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('channel', 'user')


class ChannelFavorite(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('channel', 'user')


class NewEpisode(models.Model):
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    episode_count = models.PositiveIntegerField(default=0)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('channel', 'episode_count')

class Subscriptions(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    