# Generated by Django 3.2.4 on 2022-11-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_links_code_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='refresh_time',
            field=models.IntegerField(default=10, help_text='Status check interval (in secs)'),
        ),
    ]