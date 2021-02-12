# Generated by Django 3.1.6 on 2021-02-11 19:45

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('insights', '0003_insightspagegalleryimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsightsPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='insights.insightspage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='insights_insightspagetag_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]