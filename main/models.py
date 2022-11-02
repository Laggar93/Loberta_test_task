from django.db import models


class Links(models.Model):
    class Meta:
        verbose_name = 'Links'
        verbose_name_plural = 'Links'

    link = models.URLField('Link')
    refresh_interval = models.IntegerField(default=10, help_text='Status check interval (in secs)')

    def __str__(self):
        return str(self.link)