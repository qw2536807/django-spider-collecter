# Generated by Django 3.0.1 on 2020-10-12 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collecter', '0009_auto_20201012_1712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metadata',
            old_name='metadat_name',
            new_name='metadata_name',
        ),
    ]
