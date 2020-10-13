from rest_framework import serializers
from django.contrib.postgres.fields import JSONField
from drf_yasg import openapi
import spider.tools._Getmodel as _Getmodel


from collecter.models import Metadata


class ContentField(serializers.JSONField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_OBJECT,
            "title": "元数据内容 list",
            "properties": {
                "content": openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_STRING,
                    ),
                    example=["军事", "局势"]
                ),
            }
        }


class Recode_IdField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "http://www.zhihu.com/321312321",
            "title": "记录id 为reoce表里的url",
            "max_length": _Getmodel.model_getattr(model_obj=Metadata, field='recode_id', attr='max_length')
        }


class Metadata_NameField(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "tags",
            "max_length": _Getmodel.model_getattr(model_obj=Metadata, field='metadata_name', attr='max_length')
        }


class MetadataSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metadata
        fields = ['recode_id', 'metadata_name', 'content']

    recode_id = Recode_IdField()
    metadata_name = Metadata_NameField()
    content = ContentField()


class Metadata_QuerySerializer(serializers.Serializer):

    recode_id = serializers.CharField(required=False)
    metadata_name = serializers.CharField(required=False)
    content = serializers.CharField(required=False)

