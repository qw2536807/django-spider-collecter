from rest_framework import serializers
from django.contrib.postgres.fields import JSONField
from drf_yasg import openapi


from collecter.models import Recode


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


class RecodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recode
        fields = ['title', 'domain', 'channel',
                  'url', 'description', 'content', 'updated_date']

        #read_only_fields = ['updated_date', 'created_date']
        read_only_fields = ['updated_date']


class Recode_QuerySerializer(serializers.Serializer):

    title = serializers.CharField(required=False)
    domain = serializers.CharField(required=False)
    channel = serializers.CharField(max_length=5, required=False)
