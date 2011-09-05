from __future__ import with_statement
import datetime
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from cms.models.placeholdermodel import Placeholder

from cmsplugin_blog.test.testcases import BaseBlogTestCase
from cmsplugin_blog.tests import SettingsOverride

class BlogCommetsTestCase(BaseBlogTestCase):
    
    def test_01_template_override(self):
        user = User.objects.all()[0]
        
        published_at = datetime.datetime.now() - datetime.timedelta(hours=1)
        title, entry = self.create_entry_with_title(published=True, 
            published_at=published_at, author=user)
        entry.tags = 'test'
        entry.save()

        response = self.client.get(reverse('en:blog_detail',
            kwargs={
                'year': published_at.strftime('%Y'),
                'month': published_at.strftime('%m'),
                'day': published_at.strftime('%d'),
                'slug': title.slug
            }))
        self.assertEquals(response.status_code, 200)
        self.assertContains(response, u'Comments')