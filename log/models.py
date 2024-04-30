from django.db import models
from content.models import Episode, Channel
from user_dashboard.models import CustomUser 


class ViewedContent(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(Episode, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)

class ViewedChannel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
