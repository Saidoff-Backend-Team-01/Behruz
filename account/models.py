from django.db import models
from django.contrib.auth.models import AbstractUser
from common.models import Media
from django.utils.translation import gettext_lazy as _
from common.models import Media


# Create your models here.
class User(AbstractUser):
    photo = models.OneToOneField(verbose_name=_('Photo'), to=Media, null=True, blank=True, on_delete=models.SET_NULL)
    birthday = models.DateTimeField(verbose_name=_('Birthday Data'), auto_now=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []



    def __str__(self) -> str:
        return self.username
    

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('User')
    

class Groups(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    users = models.ManyToManyField(verbose_name=_('Users'), to=User, related_name='groupusers')

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        verbose_name = _('Group')
        verbose_name_plural = _('Group')
    

class UserMessage(models.Model):
    user = models.ForeignKey(verbose_name=_('User'), to=User, on_delete=models.CASCADE)
    message = models.TextField(verbose_name=_('Message'))
    file = models.OneToOneField(verbose_name=_('File'), to=Media, on_delete=models.SET_NULL, blank=True, null=True)
    group = models.ForeignKey(verbose_name=_('Group'), to=Groups, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.user.username} - {self.group.name}"
    

    class Meta:
        verbose_name = _('User\'s message')
        verbose_name_plural = _('User\'s message')
    
