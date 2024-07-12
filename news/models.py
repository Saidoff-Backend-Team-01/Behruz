from django.db import models
from common.models import Media
from django.utils.translation import gettext_lazy as _
from news.managers import PulishedManager
# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    description = models.TextField(verbose_name=_('description'))
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    is_published = models.BooleanField(verbose_name=_('is published'), default=True)
    media_id = models.ForeignKey(to=Media, verbose_name=_('media'), null=True, on_delete=models.SET_NULL)
    published = PulishedManager() 


    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    
    def __str__(self) -> str:
        return self.title
    



