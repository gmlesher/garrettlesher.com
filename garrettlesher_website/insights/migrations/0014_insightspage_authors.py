# Generated by Django 3.1.7 on 2021-03-26 18:15

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('insights', '0013_insightsauthor'),
    ]

    operations = [
        migrations.AddField(
            model_name='insightspage',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='insights.InsightsAuthor'),
        ),
    ]
