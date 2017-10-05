from django.shortcuts import render, get_object_or_404, redirect
#from django.utils import timezone
from .models import News, Event, Gallery, Page
from .forms import NewsForm, EventForm, GalleryForm, PageForm


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

def admin(request):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    return render(request, 'schoolapp/admin.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages})

def news_new(request):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()        
    return render(request, 'schoolapp/news_edit.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages, 'form': form})

def news_edit(request, pk):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, instance=news)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'schoolapp/news_edit.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages, 'form': form})

def event_new(request):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event_data = form.save()
            return redirect('event_detail', pk=event_data.pk)
    else:
        form = EventForm()        
    return render(request, 'schoolapp/event_edit.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages, 'form': form})

def event_edit(request, pk):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    this_event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, instance=this_event)
        if form.is_valid():
            event_data = form.save()
            return redirect('event', pk=event_data.pk)
    else:
        form = EventForm(instance=this_event)
    return render(request, 'schoolapp/event_edit.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages, 'form': form})

def gallery_new(request):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    if request.method == "POST":
        form = GalleryForm(request.POST)
        if form.is_valid():
            gallery_data = form.save()
            return redirect('gallery_detail', pk=gallery_data.pk)
    else:
        form = GalleryForm()        
    return render(request, 'schoolapp/gallery_edit.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages, 'form': form})

def gallery_edit(request, pk):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    this_gallery = get_object_or_404(Gallery, pk=pk)
    if request.method == "POST":
        form = GalleryForm(request.POST, instance=this_gallery)
        if form.is_valid():
            gallery_data = form.save()
            return redirect('gallery_detail', pk=gallery_data.pk)
    else:
        form = GalleryForm(instance=this_gallery)
    return render(request, 'schoolapp/gallery_edit.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages, 'form': form})

def page_edit(request, pk):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    this_page = get_object_or_404(Page, pk=pk)
    if request.method == "POST":
        form = PageForm(request.POST, instance=this_page)
        if form.is_valid():
            page_data = form.save()
            return redirect('page', pk=page_data.pk)
    else:
        form = PageForm(instance=this_page)
    return render(request, 'schoolapp/page_edit.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages, 'form': form})
