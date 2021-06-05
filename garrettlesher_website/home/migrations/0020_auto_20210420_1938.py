# Generated by Django 3.1.7 on 2021-04-20 19:38

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20210406_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='work_content',
            field=wagtail.core.fields.StreamField([('work_heading', wagtail.core.blocks.StructBlock([('section_title', wagtail.core.blocks.CharBlock()), ('subheading', wagtail.core.blocks.CharBlock(required=False)), ('tagline', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('subheading_2', wagtail.core.blocks.CharBlock(required=False)), ('tagline_2', wagtail.core.blocks.CharBlock()), ('paragraph_2', wagtail.core.blocks.RichTextBlock(required=False))])), ('work', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('category', wagtail.core.blocks.CharBlock()), ('url', wagtail.core.blocks.URLBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())]))]),
        ),
    ]