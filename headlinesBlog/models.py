from django.db import models
from django.core.urlresolvers import reverse
"""
class Headtable(models.Model):
    #id = models.IntegerField(primary_key=True)
    head = models.TextField(blank=True)
    link = models.TextField(blank=True)
    name = models.TextField(blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    site = models.TextField(blank=True)
    day = models.TextField(blank=True)
    published = models.BooleanField(default=True)
    class Meta:
        ordering = ['-day']
        managed = False
        db_table = "headtable"
    
    def __unicode__(self):
        return u'%s' % self.head
    
    def get_absolute_url(self):
        return reverse('headlinesBlog.views.post', args=[self.slug])
"""
class Headtable(models.Model):
    #id = models.IntegerField(primary_key=True)
    head = models.CharField(max_length=150, blank=True)
    link = models.CharField(max_length=150, blank=True)
    name = models.CharField(max_length=150, blank=True)
    slug = models.SlugField(max_length=150, unique=True)
    site = models.CharField(max_length=150, blank=True)
    day = models.CharField(max_length=150, blank=True)
    published = models.CharField(max_length=150, blank=True)
    class Meta:
        ordering = ['-day']
        managed = False
        db_table = 'headtable'

    def __unicode__(self):
        return u'%s' % self.head
    
    def get_absolute_url(self):
        return reverse('headlinesBlog.views.post', args=[self.slug])