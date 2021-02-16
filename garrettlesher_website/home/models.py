from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


class HomePage(Page):
    template = "home/home_page.html"
    max_count = 1
    body = StreamField([
        ('name', blocks.CharBlock(form_classname="full title")),
        ('description', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ]) 

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
