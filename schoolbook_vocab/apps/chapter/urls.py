from django.conf.urls.defaults import *
from views import chapter_details

urlpatterns = patterns('',
#    url(r'^$', 'django.views.generic.list_detail.object_list', chapters_list_info, name='chapters_list'),
    url(r'^(?P<number>[1-9]\d*|0)/$', chapter_details, name='chapter_details')
)