from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(
        default=timezone.now
    )  # default value for date_posted will be set to current time for the first time of post creation.
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )  # Instead of storing all user detail for every post forieng key store reference to the user and on_delete specify to delete the current post if user is deleted.

    def __str__(self):
        return self.title
