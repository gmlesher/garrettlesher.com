# Generated by Django 3.1.7 on 2021-04-02 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0019_auto_20210402_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='insightsauthor',
            name='social_media',
            field=models.CharField(default='abc', max_length=100),
        ),
        migrations.AddField(
            model_name='insightsauthor',
            name='website',
            field=models.CharField(default='abc', max_length=100),
        ),
    ]