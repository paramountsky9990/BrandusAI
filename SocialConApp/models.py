from django.db import models
from django.contrib.auth.models import User

class UserSocialData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    data = models.JSONField()
    access_token = models.CharField(max_length=255)  # Store the access token

    def __str__(self):
        return f"{self.user.username} - {self.platform}"
