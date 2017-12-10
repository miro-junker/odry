from django import forms
from .models import News, Event, Gallery, Page, File


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'date', 'picture', 'perex', 'content',)

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'picture', 'since', 'to', 'info',)

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ('title', 'date', 'picture', 'path',)

class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ('title', 'content',)

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('title', 'file',)
