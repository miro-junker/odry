from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.news, name='news'),
    url(r'^novinky/strana/(?P<page>[0-9]+)/$', views.news, name='news_page'),

    url(r'^aktualita/(?P<pk>[0-9]+)/$', views.news_detail, name='news_detail'),

    url(r'^kalendar/(?P<year>[0-9]{4})-(?P<month>[0-9]{1,2})/$', views.calendar_summary, name='calendar_month'),
    url(r'^kalendar/$', views.calendar_summary, name='calendar_summary'),
    url(r'^udalost/(?P<pk>[0-9]+)/$', views.event, name='event'),

    url(r'^galerie/$', views.gallery, name='gallery'),
    url(r'^galerie/strana/(?P<page>[0-9]+)/$', views.gallery, name='gallery_page'),
    url(r'^galerie/(?P<pk>[0-9]+)/$', views.gallery_detail, name='gallery_detail'),

    url(r'^strana/(?P<pk>[0-9]+)/$', views.page, name='page'),

    # admin
    url(r'^sprava/$', views.admin, name='admin'),

    url(r'^sprava/aktualita/nova/$', views.news_new, name='news_new'),
    url(r'^sprava/aktualita/(?P<pk>[0-9]+)/$', views.news_edit, name='news_edit'),
    url(r'^sprava/aktualita/(?P<pk>[0-9]+)/smazat/$', views.news_remove, name='news_remove'),

    url(r'^sprava/udalost/nova/$', views.event_new, name='event_new'),
    url(r'^sprava/udalost/(?P<pk>[0-9]+)/$', views.event_edit, name='event_edit'),
    url(r'^sprava/udalost/(?P<pk>[0-9]+)/smazat/$', views.event_remove, name='event_remove'),

    url(r'^sprava/galerie/nova/$', views.gallery_new, name='gallery_new'),
    url(r'^sprava/galerie/(?P<pk>[0-9]+)/$', views.gallery_edit, name='gallery_edit'),
    url(r'^sprava/galerie/(?P<pk>[0-9]+)/smazat/$', views.gallery_remove, name='gallery_remove'),

    url(r'^sprava/soubory/$', views.file_edit, name='file_edit'),
    url(r'^sprava/soubor/(?P<pk>[0-9]+)/smazat$', views.file_remove, name='file_remove'),

    url(r'^sprava/strana/(?P<pk>[0-9]+)/$', views.page_edit, name='page_edit'),
]

# serve static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
studium
    obor/
    prijimaci-rizeni
    maturity
    zaverecne-zkousky

sluzby-pro-verejnost
    o-jidelne-vitkov
    jidelnicek-vitkov
    kadernictvi
    kosmetika
    masaze
    vikendove-a-prazdninove-ubytovani
    sauna

domov-mladeze
    obecne-informace
    vnitrni-rad-domova

uredni-deska
    ...
    skolni-rad

kontakty
    ...jednotliva pracoviste

formulare
'''