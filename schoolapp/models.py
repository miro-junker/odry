import os

from django.db import models
from django.utils import timezone
from django.dispatch import receiver


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
    file = models.FileField(upload_to='upload/')

    def __str__(self):
        return self.file.name



# These two auto-delete files from filesystem when they are unneeded:

@receiver(models.signals.post_delete, sender=File)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    # Deletes file from filesystem when corresponding `File` object is deleted.
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=File)
def auto_delete_file_on_change(sender, instance, **kwargs):
    # Deletes old file from filesystem when corresponding `File` object is updated with new file.
    if not instance.pk:
        return False

    try:
        old_file = MediaFile.objects.get(pk=instance.pk).file
    except MediaFile.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)