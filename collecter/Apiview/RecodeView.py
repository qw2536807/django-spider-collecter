from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

import json
from django.http import JsonResponse

from collecter.models import Recode
from collecter.serializers.RecodeSerializer import RecodeSerializer, Recode_QuerySerializer

# def get_request_args(func):
#     def _get_request_args(self, request):
#         if request.method == 'GET':
#             args = request.GET
#         else:
#             body = request.body
#             if body:
#                 try:
#                     args = json.loads(body)
#                 except Exception as e:
#                     print (e)
#                     # return makeJsonResponse(status=StatusCode.EXECUTE_FAIL, message=str(e))
#                     args = request.POST
#             else:
#                 args = request.POST
#         return func(self, request, args)

#     return _get_request_args


class RecodeView(APIView):
    '''
    get the Recode from database for now
    '''
    # id = openapi.Parameter("id", openapi.IN_QUERY, description="test manual param",
    #                        type=openapi.TYPE_INTEGER)
    # num = openapi.Parameter("num", openapi.IN_QUERY, description="test manual pssaram",
    #                         type=openapi.TYPE_INTEGER)

    @swagger_auto_schema(operation_description="partial_update description override",
                         responses={404: 'data not found',
                                    200: openapi.Response('description', RecodeSerializer)},
                         query_serializer=Recode_QuerySerializer)
    # @get_request_argsf
    def get(self, request, format=None):

        snippets = Recode.objects.filter(**request.query_params.dict())
        serializer = RecodeSerializer(snippets, many=True)

        return Response(serializer.data)

    @swagger_auto_schema(
        operation_description="apiview post description override",
        request_body=RecodeSerializer,
        security=[]
    )
    def post(self, request, format=None):

        serializer = RecodeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
