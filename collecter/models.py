from django.contrib.postgres.fields import JSONField, ArrayField
from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# 记录表
class Recode(models.Model):
    updated_date = models.DateTimeField(auto_now=True, verbose_name="更新日时")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建日时")

    title = models.CharField(max_length=100, verbose_name="内容标题")
    domain = models.CharField(max_length=100, verbose_name="域名")
    channel = models.CharField(max_length=5, verbose_name="频道")

    url = models.CharField(max_length=1000, verbose_name="url", unique=True)
    description = models.CharField(
        max_length=200, null=True, blank=True, verbose_name="Description")

    content = models.CharField(
        max_length=9999, null=True, blank=True, verbose_name="内容正文")


# 元数据

class Metadata(models.Model):
    updated_date = models.DateTimeField(auto_now=True, verbose_name="更新日时")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="创建日时")

    recode_id = models.CharField(
        max_length=1000, verbose_name="记录id 为reoce表里的url")
    metadata_name = models.CharField(
        max_length=10, verbose_name="元数据name 和recode_id为业务上的联合唯一")

    content = ArrayField(base_field=models.CharField(max_length=200),
                         verbose_name="元数据内容", blank=True, null=True)
