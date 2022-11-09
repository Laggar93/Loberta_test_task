from django.db import models


class Links(models.Model):
    class Meta:
        verbose_name = 'Links'
        verbose_name_plural = 'Links'

    link = models.URLField('Link')
    status = models.IntegerField(default=200)
    refresh_interval = models.IntegerField(default=10, help_text='Status check interval (in secs)')
    paused = models.BooleanField(default=False, help_text='Indicates whether to skip status check for the link')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.link)