from rest_framework import serializers
from common.models import Media


class MediaSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=50)
    file = serializers.FileField()


