# Generated by Django 5.0.1 on 2024-02-01 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trending', '0004_trending_anime_i1_trending_anime_i2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trending_anime',
            name='i1',
        ),
        migrations.RemoveField(
            model_name='trending_anime',
            name='i2',
        ),
        migrations.RemoveField(
            model_name='trending_anime',
            name='i3',
        ),
        migrations.RemoveField(
            model_name='trending_anime',
            name='i4',
        ),
        migrations.RemoveField(
            model_name='trending_anime',
            name='i_img',
        ),
        migrations.RemoveField(
            model_name='trending_anime',
            name='story',
        ),
        migrations.RemoveField(
            model_name='trending_anime',
            name='trend_slug',
        ),
    ]
