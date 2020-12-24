from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    """Home page model."""

    # templates = ""
    # max_count = 3
    body = RichTextField(blank=True)
    banner_title = models.CharField(max_length=100, blank=False, null=True,)


    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('body', classname="full"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"
