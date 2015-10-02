from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# encoding: utf-8

#this will assist in importing timezones
from django.utils.encoding import python_2_unicode_compatible
from django.utils.timezone import now


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

#meta tags help in stating how to display the models
class Meta:
        verbose_name = 'tag'
        verbose_name_plural = 'tags'
        ordering = ['name']

#function states that the name is returned to a string
def __str__(self):
        return self.name

class Bookmark(models.Model):
    url = models.URLField()
    title = models.CharField('title', max_length=255)
    description = models.TextField('description', blank=True)
    is_public = models.BooleanField('public', default=True)
    date_created = models.DateTimeField('date created')
    date_updated = models.DateTimeField('date updated')
    owner = models.ForeignKey(User, verbose_name='owner',
        related_name='bookmarks')
    tags = models.ManyToManyField(Tag, blank=True)

 class Meta:
        verbose_name = 'bookmark'
        verbose_name_plural = 'bookmarks'
        ordering = ['-date_created']

  #these functions return strings too
  def __str__(self):
        return '%s (%s)' % (self.title, self.url)

    def save(self, *args, **kwargs):
        if not self.id:
            self.date_created = now()
        self.date_updated = now()
        super(Bookmark, self).save(*args, **kwargs)