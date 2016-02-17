from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog/(?P<year>[0-9]{4})/$', views.year_archive),
    url(r'^blog/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.month_archive),
    url(r'^blog/post/(?P<post_id>[0-9]+)/$', views.post),
    url(r'^$', views.post_list, name='post_list'),    

]
