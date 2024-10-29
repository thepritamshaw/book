from django.db import models
from django.contrib.auth.models import User

class MediaItem(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=50)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserInteraction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    media_item = models.ForeignKey(MediaItem, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=50)  # e.g., 'viewed', 'liked'

    def __str__(self):
        return f"{self.user.username} - {self.interaction_type} - {self.media_item.title}"
