from django.conf.urls import url
from . import views

app_name = 'web'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'aboutus', views.aboutus, name='aboutus'),
    url(r'aboutrange', views.aboutrange, name='aboutrange'),
    url(r'aboutyunji', views.aboutyunji, name='aboutyunji'),
    url(r'service', views.service, name='service'),
    url(r'sereva', views.sereva, name='sereva'),
    url(r'serproduction', views.serproduction, name='serproduction'),
    url(r'serask', views.serask, name='serask'),
    url(r'serdes', views.serdes, name='serdes'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'contact', views.contact, name='contact'),
]