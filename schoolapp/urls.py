from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.news, name='news'),

     url(r'^aktualita/$', views.news_detail, name='news_detail'),

#     url(r'^kalendar$', views.calendar, name='calendar'),
#     url(r'^udalost/$', views.event, name='event'),
#     url(r'^fotogalerie$', views.gallery, name='gallery'),
#     url(r'^galerie/$', views.gallery_detail, name='gallery_detail'),
     
#     url(r'strana/^$', views.page, name='page'),


#     url(r'^admin$', views.admin, name='admin'),
#     url(r'^aktualita//edit$', views.news_edit, name='news_edit'),
#     url(r'^udalost//edit$', views.event_edit, name='event_edit'),
#     url(r'^galerie//edit$', views.gallery_edit, name='gallery_edit'),
     
#     url(r'^strana//edit$', views.page_edit, name='page_edit'),
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