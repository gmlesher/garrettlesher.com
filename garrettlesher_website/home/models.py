from django.db import models
from django.http import HttpResponse
from django.shortcuts import render
from modelcluster.fields import ParentalKey
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from django.template.response import TemplateResponse
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.contrib.forms.models import AbstractEmailForm, AbstractFormField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel

from wagtailcaptcha.models import WagtailCaptchaEmailForm


from wagtail.core import hooks

class AboutBlock(blocks.StructBlock):
    profile_image = ImageChooserBlock(required=False, label="Profile/Logo Image")
    background_image = ImageChooserBlock(label="Background Image")
    links = blocks.StructBlock([
        ('websites', blocks.StreamBlock([
            ('website_information', blocks.StructBlock([
                ('website_name', blocks.CharBlock()),
                ('website_link', blocks.URLBlock()),
                ('website_icon', ImageChooserBlock(required=False)),
                ]))
            ], max_num=2, required=False)),
        ('social_media', blocks.StreamBlock([
            ('social_media_information', blocks.StructBlock([
                ('social_media_name', blocks.CharBlock()),
                ('social_media_link', blocks.URLBlock()),
                ('social_media_icon', ImageChooserBlock(required=False)),
                ]))
            ], max_num=5, required=False, label="Social Media")),
        ('other', blocks.StreamBlock([
            ('other_information', blocks.StructBlock([
                ('other_name', blocks.CharBlock()),
                ('other_link', blocks.URLBlock()),
                ('other_icon', ImageChooserBlock(required=False)),
                ]))
            ], max_num=4, required=False)),
        ], label="Links:")
    skills = blocks.StreamBlock([
        ('skills', blocks.CharBlock()),
        ], max_num=5, label="Skills:")
    interests = blocks.StreamBlock([
        ('interests', blocks.CharBlock()),
        ], max_num=5, label="Interests:")
    who_i_am = blocks.RichTextBlock(label="Who I Am")
    what_i_do = blocks.RichTextBlock(label="What I Do")


class WorkBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    category = blocks.CharBlock()
    url = blocks.URLBlock(required=False)
    description = blocks.RichTextBlock(required=False)
    image = ImageChooserBlock()


class WorkHeading(blocks.StructBlock):
    section_title = blocks.CharBlock()
    subheading = blocks.CharBlock(required=False)
    paragraph = blocks.RichTextBlock(required=False)
    subheading_2 = blocks.CharBlock(required=False)
    paragraph_2 = blocks.RichTextBlock(required=False)


class HomePage(WagtailCaptchaEmailForm, Page):
    template = "home/home_page.html"
    max_count = 1
    body = StreamField([
        ('name', blocks.CharBlock(form_classname="full title")),
        ('description', blocks.RichTextBlock()),
    ])
    about = StreamField(
        blocks.StreamBlock([
            ('about', AboutBlock())
            ], max_num=1)
        )
    work_content = StreamField([
        ('work_heading', WorkHeading()),
        ('work', WorkBlock()),
    ])

    thank_you_text = RichTextField(blank=True)
    form_title = RichTextField(blank=True)

    content_panels = WagtailCaptchaEmailForm.content_panels + [
        StreamFieldPanel('body'),
        StreamFieldPanel('about'),
        StreamFieldPanel('work_content'),
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