from django.shortcuts import render
#from django.utils import timezone
from .models import News#, Event, Gallery, Page


def news(request):
    newss = News.objects.all()
    return render(request, 'schoolapp/news.html', {'newss': newss})

'''
def news_detail(request):
    return render(request, 'schoolapp/news_detail.html', {})

def calendar(request):
    return render(request, 'schoolapp/calendar.html', {})

def event(request):
    return render(request, 'schoolapp/event.html', {})

def gallery(request):
    return render(request, 'schoolapp/gallery.html', {})

def page(request):
    return render(request, 'schoolapp/page.html', {})

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