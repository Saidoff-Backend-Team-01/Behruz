from rest_framework import serializers
from news.models import News, NewsImage
from common.serializers import MediaSerializer


class NewsImageSerializer(serializers.Serializer):
    file = MediaSerializer()
    news = serializers.CharField()


class NewsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    created_at = serializers.DateTimeField()
    media_id = MediaSerializer()
    images = NewsImageSerializer(many=True, source='newsImage')



