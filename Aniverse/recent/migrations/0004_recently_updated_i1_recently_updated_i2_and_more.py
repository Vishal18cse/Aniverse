# Generated by Django 5.0.1 on 2024-01-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recent', '0003_recently_updated_recent_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='recently_updated',
            name='i1',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='screenshot/'),
        ),
        migrations.AddField(
            model_name='recently_updated',
            name='i2',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='screenshot/'),
        ),
        migrations.AddField(
            model_name='recently_updated',
            name='i3',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='screenshot/'),
        ),
        migrations.AddField(
            model_name='recently_updated',
            name='i4',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='screenshot/'),
        ),
        migrations.AddField(
            model_name='recently_updated',
            name='i_img',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='img/'),
        ),
        migrations.AddField(
            model_name='recently_updated',
            name='story',
            field=models.TextField(default=None, null=True),
        ),
    ]
