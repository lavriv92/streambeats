from django.db import models
from django.utils.translation import ugettext_lazy as _


class Artist(models.Model):
    """
    Performer model
    """
    name = models.CharField(_('name'), max_length=200)
    description = models.TextField(verbose_name=_('description'))
    start_active = models.DateField(verbose_name=_('start active'))
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('-created', )


class Album(models.Model):
    """
    Album model
    """
    artist = models.ForeignKey(Artist, verbose_name=_('artist'),
                               related_name='albums')
    name = models.CharField(_('name'), max_length=200)
    year = models.DateField(verbose_name=_('year'))
    description = models.TextField(verbose_name=_('description'))
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('created', )


class Track(models.Model):
    """
    Track model
    """
    name = models.CharField(_('name'), max_length=120)
    album = models.ForeignKey(Album, verbose_name=_('album'),
                              related_name='tracks')
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('created', )
