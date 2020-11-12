from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.api import APIField

class NewsPage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    # exposes to admin page to be edited
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body'),
    ]

    # exposes to API
    api_fields = [
        APIField('intro'),
        APIField('body'),
    ]