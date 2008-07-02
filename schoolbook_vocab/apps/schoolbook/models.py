from django.db import models
from apps.language.models import Language

class Schoolbook(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(prepopulate_from=("name",))
    word_language = models.ForeignKey(Language, related_name='word_schoolbooks')
    translation_language = models.ForeignKey(Language, related_name='translation_schoolbooks')
    
    class Meta:
        ordering = ('slug',)
    
    class Admin:
        list_display = ('name', 'slug')
        search_fields = ('name', 'slug')

    def __unicode__(self):
        return u'%s' % self.name
