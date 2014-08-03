from django.db import models
from django.utils.translation import ugettext_lazy as _


class FileInfoMixin(models.Model):
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
