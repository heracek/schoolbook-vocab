from django.db import models
from apps.chapter.models import Chapter

class Vocab(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='vocabs')
    word = models.CharField(max_length=100)
    
    class Meta:
        order_with_respect_to = 'chapter'
    
    class Admin:
        list_display = ('word', 'chapter')
        search_fields = ('word',)

    def __unicode__(self):
        return u'Vocab: %s' % self.word

class Translation(models.Model):
    vocab = models.ForeignKey(Vocab, related_name='translations', edit_inline=True)
    translation = models.CharField(max_length=100, core=True)
    
    class Meta:
        order_with_respect_to = 'vocab'
    
    class Admin:
        list_display = ('translation', 'vocab')
        search_fields = ('translation', 'vocab')

    def __unicode__(self):
        return self.translation
