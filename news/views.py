from rest_framework.generics import ListAPIView, RetrieveAPIView
from news.models import News
from news.serializers import NewsSerializer

# Create your views here.
class NewsList(ListAPIView):
    queryset = News.published.all()
    serializer_class = NewsSerializer


class NewsDetail(RetrieveAPIView):
    queryset = News.published.all()
    serializer_class = NewsSerializer 
