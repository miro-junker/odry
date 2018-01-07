import markdown
import bleach
import datetime
import calendar

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage
from .models import News, Event, Gallery, Page, File
from .forms import NewsForm, EventForm, GalleryForm, PageForm, FileForm


pagination_per_page = 7
pagination_orphans = 1


def get_navigator_items():
    navigator_items = {
        'news': News.objects.all().order_by('-date'),
        'event': Event.objects.all().order_by('-to'),
        'gallery': Gallery.objects.all().order_by('-date'),
        'page': Page.objects.all().order_by('title'),
    }
    return navigator_items


def news(request, page=1):
    news_all = News.objects.all().order_by('-date')
    paginator = Paginator(news_all, pagination_per_page, pagination_orphans)
    try:
        news_list = paginator.page(page)
    except EmptyPage:
        # get last page
        news_list = paginator.page(paginator.num_pages)
    return render(request, 'schoolapp/news.html', {'news_list':news_list})


def news_detail(request, pk):
    #news = News.objects.get(pk=pk)
    news = get_object_or_404(News, pk=pk)
    content_html = markdown.markdown(bleach.clean(news.content))
    return render(request, 'schoolapp/news_detail.html', {'news':news, 'content_html':content_html})


def calendar_summary(request, year=False, month=False):
    # repair invalid input
    if year==False:
        year = datetime.datetime.now().strftime("%Y")
    if month==False or int(month) > 12:
        month = datetime.datetime.now().strftime("%m")
    # find out days in month and first day
    weekdaysBeforeMonth = calendar.monthrange(int(year), int(month))[0]
    daysLeft = calendar.monthrange(int(year), int(month))[1]
    # go by days and fill in calendar
    calendar_data = []
    date_cnt = 1
    while daysLeft > 0:
        # create whole week
        week = {
            'number': datetime.date(int(year), int(month), date_cnt).isocalendar()[1],
            'days': [],
        }
        for day in range(7):
            # days in first week before actual month
            if weekdaysBeforeMonth > 0:
                week['days'].append(" ")
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
                week['days'].append(validDay)
                date_cnt += 1
                daysLeft -= 1
            # days in last week after actual month
            else:
                week['days'].append(" ")
        calendar_data.append(week)
    # calculate previous and next month
    nav = {
        'nextMonth': int(month)+1 if int(month)<12 else 1,
        'nextYear': int(year) if int(month)<12 else int(year)+1,
        'prevMonth': int(month)-1 if int(month)>1 else 12,
        'prevYear': int(year) if int(month)>1 else int(year)-1,
    }
    # get earliest event
    now = timezone.now()
    earliest = Event.objects.all().filter(to__gt=now).order_by('since')[0]
    print(earliest)
    return render(request, 'schoolapp/calendar_summary.html', {'calendar_data':calendar_data, 'year':year, 'month':month, 'nav':nav, 'earliest':earliest})


def event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    info_html = markdown.markdown(bleach.clean(event.info))
    return render(request, 'schoolapp/event.html', {'event':event, 'info_html':info_html})


def gallery(request, page=1):
    galleries_all = Gallery.objects.all().order_by('-date')
    paginator = Paginator(galleries_all, pagination_per_page, pagination_orphans)
    try:
        gallery_list = paginator.page(page)
    except EmptyPage:
        #get last page
        gallery_list = paginator.page(paginator.num_pages)
    return render(request, 'schoolapp/gallery.html', {'gallery_list':gallery_list})


def gallery_detail(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    return render(request, 'schoolapp/gallery_detail.html', {'gallery':gallery})


def page(request, pk):
    page = get_object_or_404(Page, pk=pk)
    content_html = markdown.markdown(bleach.clean(page.content))
    return render(request, 'schoolapp/page.html', {'page':page, 'content_html':content_html})


@login_required
def admin(request):
    return render(request, 'schoolapp/admin.html', {'navigator_items':get_navigator_items()})


@login_required
def news_new(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm()        
    return render(request, 'schoolapp/news_edit.html', {'navigator_items':get_navigator_items(), 'form':form})


@login_required
def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            news = form.save()
            return redirect('news_detail', pk=news.pk)
    else:
        form = NewsForm(instance=news)
    return render(request, 'schoolapp/news_edit.html', {'navigator_items':get_navigator_items(), 'form':form, 'news':news})


@login_required
def news_remove(request, pk):
    news = get_object_or_404(News, pk=pk)
    news.delete()
    return redirect('admin')

@login_required
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event_data = form.save()
            return redirect('event', pk=event_data.pk)
    else:
        form = EventForm()        
    return render(request, 'schoolapp/event_edit.html', {'navigator_items':get_navigator_items(), 'form':form})


@login_required
def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event_data = form.save()
            return redirect('event', pk=event_data.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'schoolapp/event_edit.html', {'navigator_items':get_navigator_items(), 'form':form, 'event':event})


@login_required
def event_remove(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event.delete()
    return redirect('admin')


@login_required
def gallery_new(request):
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            gallery_data = form.save()
            return redirect('gallery_detail', pk=gallery_data.pk)
    else:
        form = GalleryForm()        
    return render(request, 'schoolapp/gallery_edit.html', {'navigator_items':get_navigator_items(), 'form':form})


@login_required
def gallery_edit(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    if request.method == "POST":
        form = GalleryForm(request.POST, request.FILES, instance=gallery)
        if form.is_valid():
            gallery_data = form.save()
            # return redirect('gallery_detail', pk=gallery_data.pk)
            return redirect('gallery')
    else:
        form = GalleryForm(instance=gallery)
    return render(request, 'schoolapp/gallery_edit.html', {'navigator_items':get_navigator_items(), 'form':form, 'gallery':gallery})


@login_required
def gallery_remove(request, pk):
    gallery = get_object_or_404(Gallery, pk=pk)
    gallery.delete()
    return redirect('admin')


@login_required
def page_edit(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == "POST":
        form = PageForm(request.POST, instance=page)
        if form.is_valid():
            page_data = form.save()
            return redirect('page', pk=page_data.pk)
    else:
        form = PageForm(instance=page)
    return render(request, 'schoolapp/page_edit.html', {'navigator_items':get_navigator_items(), 'form':form, 'page':page})


@login_required
def file_edit(request):
    files = File.objects.all()
    form = FileForm()
    if request.method == "POST":
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            file_form.save()
    return render(request, 'schoolapp/file_edit.html', {'navigator_items':get_navigator_items(), 'form':form, 'files':files})


@login_required
def file_remove(request, pk):
    file = get_object_or_404(File, pk=pk)
    file.delete()
    return redirect('file_edit')