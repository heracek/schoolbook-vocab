from django.db import models
from apps.schoolbook.models import Schoolbook

class Chapter(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(prepopulate_from=("name",), unique=False)
    sub_name = models.CharField(blank=True, max_length=100)
    schoolbook = models.ForeignKey(Schoolbook, related_name='chapters')
    page = models.SmallIntegerField()
    
    class Mete:
        ordering = ('page',)
        unique_together = ('schoolbook', 'slug')
    
    class Admin:
        list_display = ('name', 'schoolbook')
        search_fields = ('name',)

    def __unicode__(self):
        return u'%s - %s' % (self.schoolbook, self.name)
