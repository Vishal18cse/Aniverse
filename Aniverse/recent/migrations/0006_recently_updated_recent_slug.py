# Generated by Django 5.0.1 on 2024-02-01 11:34

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recent', '0005_remove_recently_updated_i1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recently_updated',
            name='recent_slug',
            field=autoslug.fields.AutoSlugField(default=None, editable=False, null=True, populate_from='name', unique=True),
        ),
    ]