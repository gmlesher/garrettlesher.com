# Generated by Django 3.1.7 on 2021-03-26 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('insights', '0012_auto_20210323_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsightsAuthor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('website', models.URLField(blank=True, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'verbose_name': 'Insights Author',
                'verbose_name_plural': 'Insights Authors',
                'ordering': ['name'],
            },
        ),
    ]
