from uuid import uuid4

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from .utils import get_profile_choices, get_upload_path


class Image(models.Model):
    """
    Image model
    """
    profile = models.CharField(
        _('image profile'),
        max_length=50,
        choices=get_profile_choices()
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('owner')
    )
    file = models.ImageFiled(upload_to=get_upload_path, verbose_name=_('file'))
    uuid = models.CharField(_('uuid'), max_length=100)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        ordering = ('-created', )

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
        if not self.uuid:
            self.uuid = uuid4()

    @property
    def src(self):
        return self.file.url


class ImageThumbnail(models.Model):
    """
    Image thumnail model.
    """
    image = models.ForeignKey(Image, related_name='thumbnails')
    profile = models.CharField(_('profile'), max_length=60)
    file = models.ImageFiled(upload_to=get_upload_path, verbose_name=_('file'))
    uuid4 = models.CharField(_('uuid'), max_length=100)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    class Meta:
        verbose_name = _('image thumbnail')
        verbose_name_plural = _('image thumbnails')
        ordering = ('-created', )

    @property
    def src(self):
        return self.file.url
