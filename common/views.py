from common.serializers import MediaSerializer
from common.models import Media
from rest_framework.generics import ListAPIView
# Create your views here.


class MediaList(ListAPIView):
    serializer_class = MediaSerializer
    

    def get_queryset(self):
        queryset = Media.objects.all()
        media_type = self.request.query_params.get('type', False)  

        if media_type:
            queryset = queryset.filter(type=media_type)

        return queryset