from django.db import models
from apps.schoolbook.models import Schoolbook

class Chapter(models.Model):
    schoolbook = models.ForeignKey(Schoolbook, related_name='chapters')
    number = models.SmallIntegerField()
    name = models.CharField(max_length=100)
    sub_name = models.CharField(blank=True, max_length=100)
    
    class Mete:
        ordering = ('number',)
        unique_together = ('schoolbook', 'number')
    
    class Admin:
        list_display = ('name', 'schoolbook')
        search_fields = ('name',)

    def __unicode__(self):
        return u'%s - %s' % (self.schoolbook, self.name)
    
    def get_absolute_url(self):
        return ('chapter_details', (), { 'slug': self.slug })
    get_absolute_url = models.permalink(get_absolute_url)
