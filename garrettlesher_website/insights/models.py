from django import forms
from django.db import models, migrations
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.rich_text import RichText
from wagtail.core import blocks
from wagtail.core.blocks import RawHTMLBlock, BlockQuoteBlock 
from wagtail.embeds.blocks import EmbedBlock
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index
from wagtail.snippets.models import register_snippet


class InsightsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request, *args, **kwargs):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request, *args, **kwargs)
        blogpages = self.get_children().live().public().order_by('-first_published_at')
        context['blogpages'] = blogpages
        context['categories'] = InsightsCategory.objects.all().order_by('name')

        # Use something like this with ajax for filtering by category
        category_slug = request.GET.get('categories', None)
        if category_slug:
            categories = request.GET.get('categories')
            blogpages = blogpages.filter(categories__slug__in=[categories])

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
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name = "slug",
        allow_unicode = True,
        max_length = 255,
        help_text = "A slug to identify posts by this category",
        default = "hello",
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