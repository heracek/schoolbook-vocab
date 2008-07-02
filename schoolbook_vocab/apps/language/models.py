from django.db import models

class Language(models.Model):
    slug = models.SlugField()
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('slug',)
    
    class Admin:
        list_display = ('name', 'slug',)
        search_fields = ('name', 'slug')

    def __unicode__(self):
        return u'%s' % self.name

