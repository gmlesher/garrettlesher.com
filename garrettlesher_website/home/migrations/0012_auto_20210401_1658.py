# Generated by Django 3.1.7 on 2021-04-01 16:58

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210401_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='about',
            field=wagtail.core.fields.StreamField([('about', wagtail.core.blocks.StructBlock([('profile_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('links', wagtail.core.blocks.URLBlock(required=False)), ('skills', wagtail.core.blocks.CharBlock(required=False)), ('interests', wagtail.core.blocks.CharBlock(required=False)), ('who_i_am', wagtail.core.blocks.RichTextBlock(required=False)), ('what_i_build', wagtail.core.blocks.RichTextBlock(required=False))]))]),
        ),
    ]
