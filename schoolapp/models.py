import os

from django.db import models
from django.utils import timezone
from django.dispatch import receiver


class News(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    perex = models.TextField()
    content = models.TextField()
    picture = models.ImageField(upload_to='news/')

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    since = models.DateTimeField(default=timezone.now)
    to = models.DateTimeField(default=timezone.now)
    info = models.TextField()
    picture = models.ImageField(upload_to='events/')

    def __str__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to='gallery/')
    path = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title

class File(models.Model):
    file = models.FileField(upload_to='')

    def __str__(self):
        return self.file.name




def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)

# auto-delete files from filesystem when unneeded
@receiver(models.signals.post_delete, sender=File)
def delete_file(sender, instance, **kwargs):
    if instance.file:
        _delete_file(instance.file.path)

@receiver(models.signals.post_delete, sender=Event)
@receiver(models.signals.post_delete, sender=Gallery)
@receiver(models.signals.post_delete, sender=News)
def delete_picture(sender, instance, **kwargs):
    if instance.picture:
        _delete_file(instance.picture.path)

# auto-delete files from filesystem when updated
@receiver(models.signals.pre_save, sender=Event)
@receiver(models.signals.pre_save, sender=Gallery)
@receiver(models.signals.pre_save, sender=News)
def delete_old_picture(sender, instance, **kwargs):
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).picture
    except sender.DoesNotExist:
        return False

    new_file = instance.picture
    if not old_file == new_file:
        _delete_file(old_file.path)
