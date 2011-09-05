from django.utils.translation import ugettext_lazy as _
from django.db import models

from cmsplugin_blog.models import AbstractEntryTitle

class CommmentedEntryTitle(AbstractEntryTitle):

    comments_enabled = models.BooleanField()

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')
        
