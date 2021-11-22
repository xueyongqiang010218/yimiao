from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    class Meta:
        db_table = 'tb_user'
        verbose_name = '用户名'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Vacc(models.Model):
    name = models.CharField(max_length=50, verbose_name='名称')
    instructions = models.CharField(max_length=50, verbose_name='须知')
    address = models.CharField(max_length=50, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='联系电话')
    tag = models.CharField(max_length=50, verbose_name='接种标记')
    data = models.DateTimeField(verbose_name='接种时间',null=True)


    class Meta:
        db_table = "tb_vacc"
        verbose_name = '管理者'
        verbose_name_plural = verbose_name
