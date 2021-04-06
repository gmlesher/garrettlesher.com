# Generated by Django 3.1.7 on 2021-04-01 18:58

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_homepage_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='about',
            field=wagtail.core.fields.StreamField([('profile_image', wagtail.images.blocks.ImageChooserBlock(max_num=1)), ('about', wagtail.core.blocks.StructBlock([('profile_image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('links', wagtail.core.blocks.URLBlock(required=False)), ('skills', wagtail.core.blocks.CharBlock(required=False)), ('interests', wagtail.core.blocks.CharBlock(required=False)), ('who_i_am', wagtail.core.blocks.RichTextBlock(required=False)), ('what_i_build', wagtail.core.blocks.RichTextBlock(required=False))], max_num=1))]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='interests',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='links',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='skills',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='what_i_build',
            field=wagtail.core.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='who_i_am',
            field=wagtail.core.fields.RichTextField(),
        ),
    ]
