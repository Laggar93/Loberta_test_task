from django.contrib import admin, auth
from .models import Links


@admin.register(Links)
class LinksAdmin(admin.ModelAdmin):
    pass


admin.site.unregister(auth.models.Group)