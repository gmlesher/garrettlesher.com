# Generated by Django 3.1.7 on 2021-04-06 18:43

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_auto_20210405_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='about',
            field=wagtail.core.fields.StreamField([('about', wagtail.core.blocks.StructBlock([('profile_image', wagtail.images.blocks.ImageChooserBlock(label='Profile/Logo Image', required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock(label='Background Image')), ('links', wagtail.core.blocks.StructBlock([('websites', wagtail.core.blocks.StreamBlock([('website_information', wagtail.core.blocks.StructBlock([('website_name', wagtail.core.blocks.CharBlock()), ('website_link', wagtail.core.blocks.URLBlock()), ('website_icon', wagtail.images.blocks.ImageChooserBlock(required=False))]))], max_num=2, required=False)), ('social_media', wagtail.core.blocks.StreamBlock([('social_media_information', wagtail.core.blocks.StructBlock([('social_media_name', wagtail.core.blocks.CharBlock()), ('social_media_link', wagtail.core.blocks.URLBlock()), ('social_media_icon', wagtail.images.blocks.ImageChooserBlock(required=False))]))], label='Social Media', max_num=5, required=False)), ('other', wagtail.core.blocks.StreamBlock([('other_information', wagtail.core.blocks.StructBlock([('other_name', wagtail.core.blocks.CharBlock()), ('other_link', wagtail.core.blocks.URLBlock()), ('other_icon', wagtail.images.blocks.ImageChooserBlock(required=False))]))], max_num=4, required=False))], label='Links:')), ('skills', wagtail.core.blocks.StreamBlock([('skills', wagtail.core.blocks.CharBlock())], label='Skills:', max_num=5)), ('interests', wagtail.core.blocks.StreamBlock([('interests', wagtail.core.blocks.CharBlock())], label='Interests:', max_num=5)), ('who_i_am', wagtail.core.blocks.RichTextBlock(label='Who I Am')), ('what_i_do', wagtail.core.blocks.RichTextBlock(label='What I Do'))]))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('name', wagtail.core.blocks.CharBlock(form_classname='full title')), ('description', wagtail.core.blocks.RichTextBlock())]),
        ),
    ]
