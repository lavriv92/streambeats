from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from application.uploads.models import File, Image


class Genre(models.Model):
    """
    Genre model
    """
    name = models.CharField(_('name'), max_length=120, unique=True)
    parent = models.ForeignKey('self', verbose_name=_('parent'),
                               blank=True, null=True)
    description = models.TextField(verbose_name=_('description'))
    created = models.DateField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True),

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Artist(models.Model):
    """
    Performer model
    """
    name = models.CharField(_('name'), max_length=200)
    description = models.TextField(verbose_name=_('description'))
    image = models.ForeignKey(
        Image,
        blank=True,
        null=True,
        verbose_name=_('Image')
    )
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
    artist = models.ForeignKey(
        Artist,
        verbose_name=_('artist'),
        related_name='albums'
    )
    genre = models.ForeignKey(
        Genre,
        verbose_name=_('genre'),
        blank=True
    )
    image = models.ForeignKey(
        Image,
        verbose_name=_('Image'),
        blank=True,
        null=True
    )
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
    album = models.ForeignKey(
        Album,
        verbose_name=_('album'),
        related_name='tracks'
    )
    track_file = models.ForeignKey(
        File,
        verbose_name=_('File'),
        blank=True,
        null=True
    )
    created = models.DateTimeField(verbose_name=_('created'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('updated'), auto_now=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('created', )


class PlayList(models.Model):
    name = models.CharField(_('name'), max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              verbose_name=_('owner'))
    tracks = models.ManyToManyField(Track)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )
