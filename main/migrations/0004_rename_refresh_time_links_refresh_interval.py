# Generated by Django 3.2.4 on 2022-11-02 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_links_refresh_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='links',
            old_name='refresh_time',
            new_name='refresh_interval',
        ),
    ]
