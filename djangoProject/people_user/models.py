from django.db import models

# Create your models here.

class People(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名')
    mobile = models.CharField(max_length=11,verbose_name='手机号')
    id_number = models.CharField(max_length=18,verbose_name='身份证号码')
    address = models.CharField(max_length=50,verbose_name='家庭住址')
    unit = models.CharField(max_length=50,verbose_name='工作单位')
    password = models.CharField(max_length=20,verbose_name='密码')
    vacc_id = models.ForeignKey('users.Vacc', on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = 'tb_people'
        verbose_name = '用户名'
        verbose_name_plural = verbose_name


# 预约表
class Rescenter(models.Model):
    username = models.CharField(max_length=20,verbose_name='用户名')
    id_number = models.CharField(max_length=18, verbose_name='身份证号码')
    mobile = models.CharField(max_length=11, verbose_name='手机号')
    address = models.CharField(max_length=50, verbose_name='家庭住址')
    name = models.CharField(max_length=50, verbose_name='名称')
    vaccaddress = models.CharField(max_length=50, verbose_name='地址')
    vaccmobile = models.CharField(max_length=11, verbose_name='联系电话')
    data = models.DateTimeField(verbose_name='接种时间', null=True)
    restime = models.DateTimeField(verbose_name='预约时间',auto_now=True,null=True)
    vacc_id = models.ForeignKey('users.Vacc', on_delete=models.CASCADE,null=True)
    peo_id = models.ForeignKey('people_user.People',on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = 'tb_rescenter'
        verbose_name = '用户名'
        verbose_name_plural = verbose_name


