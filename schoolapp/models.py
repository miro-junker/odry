from django.db import models
from django.utils import timezone


class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    perex = models.TextField()
    content = models.TextField()
    picture = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    since = models.DateTimeField(default=timezone.now)
    to = models.DateTimeField(default=timezone.now)
    info = models.TextField()
    picture = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    picture = models.CharField(max_length=200)
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class File(models.Model):
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='upload/')

    def __str__(self):
        return self.file.name