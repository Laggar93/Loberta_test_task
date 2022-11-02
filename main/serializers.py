import rest_framework.serializers
from rest_framework.serializers import Serializer


class CheckStatusSerializer(Serializer):
    url = rest_framework.serializers.URLField()