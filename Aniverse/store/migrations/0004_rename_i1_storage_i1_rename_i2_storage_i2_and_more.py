# Generated by Django 5.0.1 on 2024-01-29 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_storage_i1_storage_i2_storage_i3_storage_i4_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='storage',
            old_name='I1',
            new_name='i1',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='I2',
            new_name='i2',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='I3',
            new_name='i3',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='I4',
            new_name='i4',
        ),
    ]
