from rest_framework import serializers
from django.contrib.postgres.fields import JSONField
from django.contrib.postgres.fields import ArrayField
from drf_yasg import openapi
import spider.tools._Getmodel as _Getmodel

import collecter.models as models


class ContentField(serializers.ListField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_ARRAY,
            "items": openapi.Schema(
                type=openapi.TYPE_STRING,
            ),
            'example': ["军事", "局势"],
            "title": "元数据内容 list"
        }


class Recode_IdField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "http://www.zhihu.com/321312321",
            "title": "记录id 为reoce表里的url",
            "max_length": _Getmodel.model_getattr(model_obj=models.Metadata, field='recode_id', attr='max_length')
        }


class Metadata_NameField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "tags",
            "max_length": _Getmodel.model_getattr(model_obj=models.Metadata, field='metadata_name', attr='max_length')
        }


class MetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Metadata
        fields = ['recode_id', 'metadata_name', 'content']

    recode_id = Recode_IdField()
    metadata_name = Metadata_NameField()
    content = ContentField()


class Metadata_QuerySerializer(serializers.Serializer):

    recode_id = serializers.CharField(required=False)
    metadata_name = serializers.CharField(required=False)
    content = serializers.CharField(required=False)
