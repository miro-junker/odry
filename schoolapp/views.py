from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
#from django.utils import timezone
from .models import News, Event, Gallery, Page
from .forms import NewsForm, EventForm, GalleryForm, PageForm

import markdown
import bleach
import datetime
import calendar


def homepage(request):
    newss = News.objects.all()
    return render(request, 'schoolapp/homepage.html', {'newss': newss})


def news_detail(request, pk):
    #news = News.objects.get(pk=pk)
    news = get_object_or_404(News, pk=pk)
    content_html = markdown.markdown(bleach.clean(news.content))
    return render(request, 'schoolapp/news_detail.html', {'news': news, 'content_html': content_html})


def calendar_summary(request, year=False, month=False):
    # repair invalid input
    if year==False:
        year = datetime.datetime.now().strftime("%Y")
    if month==False or int(month) > 12:
        month = datetime.datetime.now().strftime("%m")
    # find out days in month and first day
    weekdaysBeforeMonth = calendar.monthrange(int(year), int(month))[0]
    daysLeft = calendar.monthrange(int(year), int(month))[1]
    # 
    calendar_data = []
    date_cnt = 1
    while daysLeft > 0:
        # create whole week
        week = []
        for day in range(7):
            # days in first week before actual month
            if weekdaysBeforeMonth > 0:
                week.append(" ")
                weekdaysBeforeMonth -= 1
            # valid days in month
            elif daysLeft > 0:
                morning = datetime.datetime(int(year), int(month), date_cnt)
                tomorrowMorning = morning + datetime.timedelta(days = 1)
                events = Event.objects.all().filter(since__lt=tomorrowMorning).filter(to__gte=morning)
                validDay = {
                    'number': date_cnt,
                    'events': events,
                }
                week.append(validDay)
                date_cnt += 1
                daysLeft -= 1
            # days in last week after actual month
            else:
                week.append(" ")
        calendar_data.append(week)
    # calculate previous and next month
    nav = {
        'nextMonth': int(month)+1 if int(month)<12 else 1,
        'nextYear': int(year) if int(month)<12 else int(year)+1,
        'prevMonth': int(month)-1 if int(month)>1 else 12,
        'prevYear': int(year) if int(month)>1 else int(year)-1,
    }
    return render(request, 'schoolapp/calendar_summary.html', {'calendar_data': calendar_data, 'year': year, 'month': month, 'nav': nav})


def event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    info_html = markdown.markdown(bleach.clean(event.info))
    return render(request, 'schoolapp/event.html', {'event': event, 'info_html': info_html})


def gallery(request):
    gallerys = Gallery.objects.all()
    return render(request, 'schoolapp/gallery.html', {'gallerys': gallerys})


def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    return render(request, 'schoolapp/gallery_detail.html', {'gallery': gallery})


def page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    content_html = markdown.markdown(bleach.clean(page.content))
    return render(request, 'schoolapp/page.html', {'page': page, 'content_html': content_html})


@login_required
def admin(request):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    return render(request, 'schoolapp/admin.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages})


@login_required
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


@login_required
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


@login_required
def news_remove(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('admin')

@login_required
def event_new(request):
    newss = News.objects.all()
    events = Event.objects.all()
    gallerys = Gallery.objects.all()
    pages = Page.objects.all()
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            event_data = form.save()
            return redirect('event', pk=event_data.pk)
    else:
        form = EventForm()        
    return render(request, 'schoolapp/event_edit.html', {'newss': newss, 'events': events, 'gallerys': gallerys, 'pages': pages, 'form': form})


@login_required
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


@login_required
def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('admin')


@login_required
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


@login_required
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


@login_required
def gallery_remove(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    gallery.delete()
    return redirect('admin')


@login_required
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
