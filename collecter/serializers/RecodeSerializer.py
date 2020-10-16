from rest_framework import serializers
from django.contrib.postgres.fields import JSONField
from drf_yasg import openapi


from collecter.models import Recode

import collecter.models as models


import spider.tools._Getmodel as _Getmodel

# class RecodeField(serializers.JSONField):
#     class Meta:
#         swagger_schema_fields = {
#             "type": openapi.TYPE_OBJECT,
#             "title": "Metadata",
#             "properties": {
#                 "metadata": openapi.Schema(
#                     title="metadata",
#                     type=openapi.TYPE_ARRAY,
#                     items=openapi.Schema(
#                         type=openapi.TYPE_OBJECT,
#                     ),
#                     default=[
#                         {"type": "1", "name": "index", "value": "1"},
#                         {"type": "2", "name": "Clicks", "value": "1444754"},
#                         {"type": "3", "name": "question_type", "value": "army"}
#                     ]
#                 ),
#             }
#         }


class Title_Field(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "如何评价XXXXX",
            "title": "记录标题",
            "max_length": _Getmodel.model_getattr(model_obj=models.Recode, field='title', attr='max_length'),
        }


class Domain_Field(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "www.zhihu.com",
            "title": "记录Domain",
            "max_length": _Getmodel.model_getattr(model_obj=models.Recode, field='domain', attr='max_length')
        }


class Channel_Field(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "1",
            "title": "记录频道",
            "max_length": _Getmodel.model_getattr(model_obj=models.Recode, field='channel', attr='max_length'),
            "allow_null": _Getmodel.model_getattr(model_obj=models.Recode, field='channel', attr='null'),
            "allow_blank": _Getmodel.model_getattr(model_obj=models.Recode, field='channel', attr='blank')
        }


class Url_Field(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "http://www.zhihu.com/321312321",
            "title": "记录地址",
            "max_length": _Getmodel.model_getattr(model_obj=models.Recode, field='url', attr='max_length'),
            "allow_null": _Getmodel.model_getattr(model_obj=models.Recode, field='url', attr='null'),
            "allow_blank": _Getmodel.model_getattr(model_obj=models.Recode, field='url', attr='blank')
        }


class Description_Field(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "O泡果奶",
            "title": "描述",
            "max_length": _Getmodel.model_getattr(model_obj=models.Recode, field='description', attr='max_length'),
            "allow_null": _Getmodel.model_getattr(model_obj=models.Recode, field='description', attr='null'),
            "allow_blank": _Getmodel.model_getattr(model_obj=models.Recode, field='description', attr='blank')

        }


class Content_Field(serializers.CharField):
    class Meta:
        swagger_schema_fields = {
            "type": openapi.TYPE_STRING,
            "example": "内容",
            "title": "内容",
            "max_length": _Getmodel.model_getattr(model_obj=models.Recode, field='content', attr='max_length'),
            "allow_null": _Getmodel.model_getattr(model_obj=models.Recode, field='content', attr='null'),
            "allow_blank": _Getmodel.model_getattr(model_obj=models.Recode, field='content', attr='blank')
        }


class RecodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Recode
        fields = ['title', 'domain', 'channel',
                  'url', 'description', 'content', 'updated_date']

        #read_only_fields = ['updated_date', 'created_date']
        read_only_fields = ['updated_date']

    title = Title_Field()
    domain = Domain_Field()
    channel = Channel_Field()
    url = Url_Field()
    description = Description_Field(required=False)
    content = Content_Field(required=False)


class Recode_QuerySerializer(serializers.Serializer):

    title = serializers.CharField(required=False)
    domain = serializers.CharField(required=False)
    channel = serializers.CharField(max_length=5, required=False)
