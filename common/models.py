from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

# Create your models here.
class Media(models.Model):
    class MediaType(models.TextChoices):
        IMAGE = 'image', _('image')
        MUSIC = 'music', _('video')
        AUDIO = 'audio', _('audio')
        FILE = 'file', _('file')
        VIDEO = 'video', _('video')

    
    type = models.CharField(verbose_name=_('type'), max_length=30, choices=MediaType.choices)
    file = models.FileField(verbose_name=_('file'), upload_to='media/') 


    def clean(self):
        if not self.type in self.MediaType.values:
            raise ValidationError('This type doesn`t exist')
        
        elif self.type == self.MediaType.IMAGE and not self.file.name.split('.')[-1] in ['jpeg', 'png', 'gif', 'svg', 'bmp', 'tiff']:
            raise ValidationError(f'{self.file.name.split(".")[-1]} {_("is not image format")}')

        elif self.type == self.MediaType.VIDEO and not self.file.name.split('.')[-1] in ['mp4', 'avi', 'mkv', 'mov', 'wmv', 'flv']:
            raise ValidationError(f'{self.file.name.split(".")[-1]} {_("is not video format")}')

        elif self.type == self.MediaType.FILE and not self.file.name.split('.')[-1] in ['pdf', 'docx', 'xlsx', 'pptx', 'txt', 'csv']:
            raise ValidationError(f'{self.file.name.split(".")[-1]} {_("is not file format")}')

        elif self.type == self.MediaType.AUDIO and not self.file.name.split('.')[-1] in ['mp3', 'wav', 'flac', 'aac', 'ogg', 'wma']:
            raise ValidationError(f'{self.file.name.split(".")[-1]} {_("is not audio format")}')

        elif self.type == self.MediaType.MUSIC and not self.file.name.split('.')[-1] in ['mp3', 'flac', 'aac', 'wav', 'ogg']:
            raise ValidationError(f'{self.file.name.split(".")[-1]} {_("is not music format")}')
        
    def __str__(self) -> str:
        return self.type


    class Meta:
        verbose_name = _('Media')
        verbose_name_plural = _('Media')    