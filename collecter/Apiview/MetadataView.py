from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import json
from django.http import JsonResponse

from collecter.models import Metadata
from collecter.serializers.MetadataSerializer import MetadataSerializer, Metadata_QuerySerializer


class MetadataView(APIView):
    '''
    get the Metadata from database for now
    '''
    @swagger_auto_schema(operation_description="partial_update description override",
                         responses={404: 'data not found', 200: openapi.Response(
                             'description', MetadataSerializer)},
                         query_serializer=Metadata_QuerySerializer,
                         example="dsadsa")
    # @get_request_args
    def get(self, request, format=None):

        snippets = Metadata.objects.filter(**request.query_params.dict())
        serializer = MetadataSerializer(snippets, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=MetadataSerializer,
        security=[],
    )
    def post(self, request, format=None):

        serializer = MetadataSerializer(data=request.data)

        # todo create or update
        #
        #
        #
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
