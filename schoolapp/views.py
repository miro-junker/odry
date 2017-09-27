from django.shortcuts import render, get_object_or_404
#from django.utils import timezone
from .models import News, Event, Gallery, Page


def homepage(request):
    newss = News.objects.all()
    return render(request, 'schoolapp/homepage.html', {'newss': newss})

def news_detail(request, pk):
    #news = News.objects.get(pk=pk)
    news = get_object_or_404(News, pk=pk)
    return render(request, 'schoolapp/news_detail.html', {'news': news})

def calendar(request):
    events = Event.objects.all()
    return render(request, 'schoolapp/calendar.html', {'events': events})

def event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    return render(request, 'schoolapp/event.html', {'event': event})

def gallery(request):
    gallerys = Gallery.objects.all()
    return render(request, 'schoolapp/gallery.html', {'gallerys': gallerys})


def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    return render(request, 'schoolapp/gallery_detail.html', {'gallery': gallery})

def page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'schoolapp/page.html', {'page': page})

'''
def admin(request):
    return render(request, 'schoolapp/admin.html', {})

def news_edit(request):
    return render(request, 'schoolapp/news_edit.html', {})

def event_edit(request):
    return render(request, 'schoolapp/event_edit.html', {})

def gallery_edit(request):
    return render(request, 'schoolapp/gallery_edit.html', {})

def page_edit(request):
    return render(request, 'schoolapp/page_edit.html', {})
'''