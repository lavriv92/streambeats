from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.translation import ugettext_lazy as _

from .utils import get_upload_path


class Image(models.Model):
    """
    Image model
    """
    ALBUM = 'album'
    ARTIST = 'artist'
    USER = 'user'

    TYPES = (
        (ALBUM, _('Album')),
        (ARTIST, _('Artist')),
        (USER, _('User')),
    )

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner')
    )
    image_type = models.CharField(max_length=50, choices=TYPES)
    image = models.FileField(
        upload_to=get_upload_path('images'),
        verbose_name=_('image')
    )
    thumbnail = models.FileField(
        upload_to=get_upload_path('thumbnails'),
        blank=True, null=True,
        verbose_name=_('thumbnail')
    )
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        ordering = ('-created', )

    @property
    def src(self):
        return self.image.url


class File(models.Model):
    """
    File model
    """
    file = models.FileField(
        upload_to=get_upload_path('files'),
        verbose_name=_('File')
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    @property
    def src(self):
        return self.file.url

    class Meta:
        ordering = ('-created', )


@receiver(pre_save, sender=Image)
def upload_path(sender, **kwargs):
    pass
