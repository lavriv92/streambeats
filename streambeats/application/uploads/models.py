from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

class Image(models.Model):
    profile = models.CharField(
        _('image profile'),
        max_length=50,
        choices=get_profile_choices()
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    file = models.ImageFiled(upload_to=get_upload_path)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('updated'), auto_now=True)

    @property
    def src(self):
        return self.file.url


class ImageThumbnail(models.Model):
    image = models.ForeignKey(Image, related_name='thumbnails')
    file = models.ImageFiled(upload_to=get_upload_path)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class File(models.Model):
    """
    Base file model.
    """
    name = models.CharField(_('name'), max_length=120)
    size = models.FloatField(_('size'), default=0)
    created = models.DateTimeField(_('created'), auto_now_add=True)
    updated = models.DateTimeField(_('created'), auto_now=True)

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')
        ordering = _('-created')

    def __unicode__(self):
        return self.name
