# Generated by Django 3.1.6 on 2021-03-10 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20210310_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='intro',
        ),
    ]
