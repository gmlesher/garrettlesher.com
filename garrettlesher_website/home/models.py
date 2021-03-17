from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel




from wagtail.core import hooks


class HomePage(AbstractEmailForm, Page):
    template = "home/home_page.html"
    ajax_template = "home/home_page_ajax.html"
    max_count = 1
    body = StreamField([
        ('name', blocks.CharBlock(form_classname="full title")),
        ('description', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ]) 

    # work = StreamField([
    #     ('name', blocks.CharBlock(form_classname="full title", default="hello")),
    #     ('description', blocks.RichTextBlock(default="hello")),
    # ])

    thank_you_text = RichTextField(blank=True)
    form_title = RichTextField(blank=True)

    content_panels = AbstractEmailForm.content_panels + [
        StreamFieldPanel('body'),
        # StreamFieldPanel('work'),
        FieldPanel('form_title', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel('subject'),
        ], "Email settings"),
        FormSubmissionsPanel('Contact form submissions'),
    ]



class FormField(AbstractFormField):
    page = ParentalKey('HomePage', on_delete=models.CASCADE, related_name='form_fields')