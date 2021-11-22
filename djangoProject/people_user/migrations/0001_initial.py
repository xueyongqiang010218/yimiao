# Generated by Django 3.2.8 on 2021-11-19 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('id_number', models.CharField(max_length=18, verbose_name='身份证号码')),
                ('address', models.CharField(max_length=50, verbose_name='家庭住址')),
                ('unit', models.CharField(max_length=50, verbose_name='工作单位')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户名',
                'verbose_name_plural': '用户名',
                'db_table': 'tb_people',
            },
        ),
        migrations.CreateModel(
            name='Rescenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20, verbose_name='用户名')),
                ('id_number', models.CharField(max_length=18, verbose_name='身份证号码')),
                ('mobile', models.CharField(max_length=11, verbose_name='手机号')),
                ('address', models.CharField(max_length=50, verbose_name='家庭住址')),
                ('name', models.CharField(max_length=50, verbose_name='名称')),
                ('vaccaddress', models.CharField(max_length=50, verbose_name='地址')),
                ('vaccmobile', models.CharField(max_length=11, verbose_name='联系电话')),
                ('data', models.DateTimeField(null=True, verbose_name='接种时间')),
                ('restime', models.DateTimeField(auto_now=True, null=True, verbose_name='预约时间')),
                ('peo_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='people_user.people')),
            ],
            options={
                'verbose_name': '用户名',
                'verbose_name_plural': '用户名',
                'db_table': 'tb_rescenter',
            },
        ),
    ]