from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import json

#Importacion del modelo y tabla
from loadImage.models import ImgModel
from loadImage.serializers import TablaImg

#Importacion de metodo ResponseCustom
from primerComponente.views import ResponseCustom

#Variables Globales

responseOk = '{"messages":"success"}'
responseOk = json.loads(responseOk)

responseBad = '{"messages":"error"}'
responseBad = json.loads(responseBad)

# Create your views here.
class ViewListImg(APIView):
    def get(self, request, format=None):
        queryset = ImgModel.objects.all()
        serializer = TablaImg(queryset, many=True, context={'request':request})
        return ResponseCustom.response_custom(serializer.data, responseOk, status.HTTP_200_OK)

    def post(self, request, format=None):
        
        format_split = str(request.data['url_img']).split('.')
        
        request.data['name_img'] = format_split[0]
        request.data['format_img'] = format_split[1]
        
        serializer = TablaImg(data=request.data)
    
        if serializer.is_valid():
            serializer.save()
            return ResponseCustom.response_custom(serializer.data, responseOk, status.HTTP_201_CREATED)
        
        else:
            return ResponseCustom.response_custom(serializer.errors, responseBad, status.HTTP_400_BAD_REQUEST)


class ViewDetailImg(APIView):
    def get_object(self, pk):
        try:
            return ImgModel.objects.get(pk=pk)
        except ImgModel.DoesNotExist:
            return 404
        
    def put(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            serializer = TablaImg(idResponse, data=request.data, context={'request': request})
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
            idResponse.url_img.delete()
            idResponse.delete()
            return Response(responseOk)
        else:
            return Response(responseBad) 

