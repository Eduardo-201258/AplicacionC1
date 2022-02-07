from logging import error
from urllib import response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

#importacion de los componentes a utilizar
from primerComponente.models import PrimerModelo
from primerComponente.serializers import PrimerTablaSerializer
import json

responseOk = '{"messages":"success"}'
responseOk = json.loads(responseOk)

responseBad = '{"messages":"error"}'
responseBad = json.loads(responseBad)

# Create your views here.
class PrimerViewList(APIView):
    
    def get(self, request, format=None):
        queryset = PrimerModelo.objects.all()
        serializer = PrimerTablaSerializer(queryset, many=True, context={'request':request})
        
        return ResponseCustom.response_custom(serializer.data, responseOk, status.HTTP_200_OK)
    
    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data=request.data, context ={'request':request})
        if serializer.is_valid():
            serializer.save()

            return ResponseCustom.response_custom(serializer.data, responseOk, status.HTTP_201_CREATED)
        else:
            
            return ResponseCustom.response_custom(serializer.errors, responseBad, status.HTTP_400_BAD_REQUEST)
        
        
class PrimerViewDetail(APIView):
    def get_object(self, pk):
        try:
            return PrimerModelo.objects.get(pk=pk)
        except PrimerModelo.DoesNotExist:
            return 404
    
    def get(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, context={'request':request})
            return ResponseCustom.response_custom(serializer.data, responseOk, status=status.HTTP_200_OK)
        return ResponseCustom.response_custom("No encontrado", 'error', status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return ResponseCustom.response_custom(serializer.data, responseOk, status.HTTP_200_OK)
            else:
                return ResponseCustom.response_custom(serializer.data, responseBad, status.HTTP_400_BAD_REQUEST)
        else:
            return Response(responseBad)
        
    def delete(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            idResponse.delete()
            return Response(responseOk)
        else:
            return Response(responseBad)

    
class ResponseCustom():
    def response_custom(response, message, status):
        response = ( message, {
                "pay_load": response,
                "status": status
        })
            
        return Response(response)