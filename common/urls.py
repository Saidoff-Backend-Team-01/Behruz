from django.urls import path
from common.views import MediaList


urlpatterns = [
    path('medialist/', MediaList.as_view(), name='medialist'),
]