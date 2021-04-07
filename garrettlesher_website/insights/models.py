""" python imports"""

""" django imports """
from django import forms
from django.db import models, migrations

""" wagtail imports """
# wagtail embeds
from wagtail.embeds.blocks import EmbedBlock
# wagtail snippets
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
# wagtail images
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
# wagtail search
from wagtail.search import index
#  wagtail admin
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
# wagtail core
from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.rich_text import RichText
from wagtail.core.blocks import RawHTMLBlock, BlockQuoteBlock 

""" 3rd party app imports"""
#  model cluster
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
# taggit
from taggit.models import TaggedItemBase


class InsightsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request, *args, **kwargs)
        blogpages = InsightsPage.objects.live().public().order_by('-first_published_at')
        category_slug = request.GET.get('category', None)
        if category_slug:
            if blogpages.filter(categories__slug=category_slug).count() > 0:
                context['blogpages'] = blogpages.filter(categories__slug=category_slug)
        else:
            context['blogpages'] = blogpages

        context['category_slug'] = category_slug
        context['authors'] = InsightsAuthor.objects.all()
        context['categories'] = InsightsCategory.objects.all().order_by('name')

        return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
    ]

class InsightsPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'InsightsPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class InsightsPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('raw_HTML', RawHTMLBlock()),
        ('block_quote', BlockQuoteBlock()),
        ('embed', EmbedBlock()),
    ])
    tags = ClusterTaggableManager(through=InsightsPageTag, blank=True)
    categories = ParentalManyToManyField('insights.InsightsCategory', blank=True)
    authors = ParentalManyToManyField('insights.InsightsAuthor', blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
             return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        MultiFieldPanel([
            InlinePanel('insights_authors', label="Author", min_num=1, max_num=4)
            ], heading="Authors"),
        FieldPanel('intro'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class InsightsPageGalleryImage(Orderable):
    page = ParentalKey(InsightsPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class InsightsAuthorsOrderable(Orderable):
    """allows selection of one or more authors for insights post"""

    page = ParentalKey(InsightsPage, on_delete=models.CASCADE, related_name='insights_authors')
    author = models.ForeignKey(
        "insights.InsightsAuthor", 
        on_delete=models.CASCADE,
        related_name='+',
        )

    panels = [
        SnippetChooserPanel("author"),
    ]


class InsightsTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = InsightsPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['insights_index'] = InsightsIndexPage.objects.first()
        context['blogpages'] = blogpages
        return context
    

@register_snippet
class InsightsCategory(models.Model):
    """Insights category snippets"""
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name = "slug",
        allow_unicode = True,
        max_length = 255,
        help_text = "A slug to identify posts by this category",
    )
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )


    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Insights Category"
        verbose_name_plural = 'Insights Categories'
        ordering = ["name"]

# StructBlocks
class WebsiteBlock(blocks.StructBlock):
    website_name = blocks.CharBlock()
    website_link = blocks.URLBlock()


class SocialMediaBlock(blocks.StructBlock):
    social_media_name = blocks.CharBlock()
    social_media_link = blocks.URLBlock()


@register_snippet
class InsightsAuthor(models.Model):
    """Insights author snippets"""
    name = models.CharField(max_length=100)
    website = StreamField([
        ('website_block', WebsiteBlock(max_num=1)),
        ], blank=True, null=True)
    social_media = StreamField([
        ('social_media_block', SocialMediaBlock()),
        ], blank=True, null=True, verbose_name="Social Media & Other") 
    image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        null=True,
        blank=True, 
        related_name="+",
        )

    panels = [
        MultiFieldPanel([
            FieldPanel("name"),
            ImageChooserPanel("image"),

            ], heading="Name and Image"),
        MultiFieldPanel([
            StreamFieldPanel("website"),
            StreamFieldPanel("social_media"),
            ], heading="Links"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Insights Author"
        verbose_name_plural = 'Insights Authors'
        ordering = ["name"]

