# Generated by Django 3.2.4 on 2022-11-02 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Link')),
                ('code_status', models.CharField(max_length=50, verbose_name='Code status')),
                ('refresh_time', models.DateTimeField(null=True, verbose_name='Refresh time')),
            ],
            options={
                'verbose_name': 'Links',
                'verbose_name_plural': 'Links',
            },
        ),
    ]