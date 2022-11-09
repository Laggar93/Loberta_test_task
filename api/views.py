from rest_framework import viewsets
from api.serializers import LinkSerializer
from links.models import Links


class LinksViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Links.objects.all()
    serializer_class = LinkSerializer
