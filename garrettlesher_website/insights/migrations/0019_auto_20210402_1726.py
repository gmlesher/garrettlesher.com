# Generated by Django 3.1.7 on 2021-04-02 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0018_auto_20210401_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='insightsauthor',
            name='social_media',
        ),
        migrations.RemoveField(
            model_name='insightsauthor',
            name='website',
        ),
    ]
