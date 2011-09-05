from django.utils.translation import ugettext_lazy as _
from django.db import models

from cmsplugin_blog.models import AbstractEntryTitle

class CommentedEntryTitle(AbstractEntryTitle):

    DETAIL_TEMPLATE = 'cmsplugin_blog/entry_detail_threadedcomments.html'

    comments_enabled = models.BooleanField()

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entries')

        
