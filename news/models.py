from django.db import models
from common.models import Media
from django.utils.translation import gettext_lazy as _
from news.managers import PulishedManager
from ckeditor.fields import RichTextField
# Create your models here.


class News(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255)
    description = RichTextField(verbose_name=_('description'))
    created_at = models.DateTimeField(verbose_name=_('created at'), auto_now_add=True)
    is_published = models.BooleanField(verbose_name=_('is published'), default=True)
    media_id = models.ForeignKey(to=Media, verbose_name=_('media'), null=True, on_delete=models.SET_NULL)
    published = PulishedManager() 


    class Meta:
        verbose_name = _('News')
        verbose_name_plural = _('News')

    
    def __str__(self) -> str:
        return self.title
    


class NewsImage(models.Model):
    file = models.OneToOneField(to=Media, verbose_name=_('file'), on_delete=models.CASCADE)
    news = models.ForeignKey(to=News, verbose_name=_('news'), on_delete=models.CASCADE, related_name='newsImage')


    def __str__(self) -> str:
        return self.news.title
    

    class Meta:
        verbose_name = _('News Image')
        verbose_name_plural = _('News Images')
        

