# Generated by Django 3.2.4 on 2022-11-09 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_seed'),
    ]

    operations = [
        migrations.AddField(
            model_name='links',
            name='paused',
            field=models.BooleanField(default=False, help_text='Indicates whether to skip status check for the link'),
        ),
        migrations.AddField(
            model_name='links',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
