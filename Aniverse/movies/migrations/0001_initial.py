# Generated by Django 5.0.1 on 2024-01-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='anime_movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('dic', models.CharField(max_length=250)),
                ('img', models.FileField(default=None, null=True, upload_to='anime_movies/')),
            ],
        ),
    ]