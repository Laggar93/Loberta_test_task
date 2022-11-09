from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from links.models import Links


class IndexView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    queryset = Links.objects.all()
    context_object_name = 'links'
