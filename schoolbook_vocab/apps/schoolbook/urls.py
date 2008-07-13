from django.conf.urls.defaults import *
from models import Schoolbook

schoolbooks_list_info = {
    'queryset': Schoolbook.objects.all()
}

urlpatterns = patterns('',
    url(r'^$', 'django.views.generic.list_detail.object_list', schoolbooks_list_info, name='schoolbooks_list'),
    url(r'^(?P<slug>[0-9A-Za-z-]+)/$', 'django.views.generic.list_detail.object_detail', schoolbooks_list_info, name='schoolbook_details')
)