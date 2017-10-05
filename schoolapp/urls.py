from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.homepage, name='homepage'),

     url(r'^aktualita/(?P<pk>[0-9]+)/$', views.news_detail, name='news_detail'),
     url(r'^kalendar/$', views.calendar, name='calendar'),
     url(r'^udalost/(?P<pk>[0-9]+)/$', views.event, name='event'),
     url(r'^galerie/$', views.gallery, name='gallery'),
     url(r'^galerie/(?P<pk>[0-9]+)/$', views.gallery_detail, name='gallery_detail'),
     
     url(r'^strana/(?P<pk>[0-9]+)/$', views.page, name='page'),


     url(r'^sprava/$', views.admin, name='admin'),
     
     url(r'^pridat/aktualita/$', views.news_new, name='news_new'),
     url(r'^aktualita/(?P<pk>[0-9]+)/edit/$', views.news_edit, name='news_edit'),

     url(r'^pridat/udalost/$', views.event_new, name='event_new'),
     url(r'^udalost/(?P<pk>[0-9]+)/edit/$', views.event_edit, name='event_edit'),


     url(r'^pridat/galerie/$', views.gallery_new, name='gallery_new'),
     url(r'^galerie/(?P<pk>[0-9]+)/edit/$', views.gallery_edit, name='gallery_edit'),
     
     url(r'^strana/(?P<pk>[0-9]+)/edit/$', views.page_edit, name='page_edit'),
]

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