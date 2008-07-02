from django.conf.urls.defaults import *

urlpatterns = patterns('',
    # Example:
    # (r'^schoolbook_vocab/', include('schoolbook_vocab.foo.urls')),

    # Uncomment this for admin:
    (r'^admin/', include('django.contrib.admin.urls')),
)
