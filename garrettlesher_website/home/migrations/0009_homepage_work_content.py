# Generated by Django 3.1.7 on 2021-03-23 19:26

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_homepage_form_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='work_content',
            field=wagtail.core.fields.RichTextField(default='hello'),
        ),
    ]