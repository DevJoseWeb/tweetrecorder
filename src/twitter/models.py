from django.db import models


class Tweet(models.Model):
    id_str = models.CharField(max_length=255, unique=True)
    text = models.CharField(max_length=255)
    author = models.CharField(max_length=255)

