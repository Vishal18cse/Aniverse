# Generated by Django 5.0.1 on 2024-01-28 09:37

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trending', '0002_alter_trending_anime_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending_anime',
            name='trend_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]
