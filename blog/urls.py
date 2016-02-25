from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^(?P<year>[0-9]{4})/$', views.year_archive, name='year_archive'),
    url(r'^(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive, name='month_archive'),
    url(r'^post/(?P<post_id>[0-9]+)/$', views.post, name='post'),
    url(r'^$', views.post_list, name='post_list'),    
]
