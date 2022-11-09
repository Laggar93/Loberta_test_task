from rest_framework.serializers import ModelSerializer
from links.models import Links


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Links
        fields = ('id', 'link', 'status')