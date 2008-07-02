from django.db import models
from apps.schoolbook.models import Schoolbook

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(prepopulate_from=("name",))
    sub_name = models.CharField(blank=True, max_length=100)
    schoolbook = models.ForeignKey(Schoolbook)
    ordering = models.IntegerField(default=0)
    
    class Mete:
        ordering = ('ordering',)
    
    class Admin:
        list_display = ('name', 'schoolbook')
        search_fields = ('name',)

    def __unicode__(self):
        return u'%s - %s' % (self.schoolbook, self.name)
