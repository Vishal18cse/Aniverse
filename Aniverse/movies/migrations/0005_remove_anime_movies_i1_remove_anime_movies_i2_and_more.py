# Generated by Django 5.0.1 on 2024-02-01 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_rename_dic_anime_movies_dis_anime_movies_i1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime_movies',
            name='i1',
        ),
        migrations.RemoveField(
            model_name='anime_movies',
            name='i2',
        ),
        migrations.RemoveField(
            model_name='anime_movies',
            name='i3',
        ),
        migrations.RemoveField(
            model_name='anime_movies',
            name='i4',
        ),
        migrations.RemoveField(
            model_name='anime_movies',
            name='i_img',
        ),
        migrations.RemoveField(
            model_name='anime_movies',
            name='story',
        ),
    ]
