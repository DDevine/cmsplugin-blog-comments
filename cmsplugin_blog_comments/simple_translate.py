from cmsplugin_blog.models import Entry
from cmsplugin_blog_comments import CommentedEntryTitle
from simple_translation.translation_pool import translation_pool

translation_pool.unregister_translation(Entry)
translation_pool.register_translation(Entry, CommentedEntryTitle)
