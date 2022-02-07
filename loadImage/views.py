from os import sep
from unicodedata import name
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from loadImage.models import ImgModel
from loadImage.serializers import TablaImg
import json

# Create your views here.
class ViewListImg(APIView):
    def get(self, request, format=None):
        queryset = ImgModel.objects.all()
        serializer = TablaImg(queryset, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        
        parseo = str(request.data['url_img'])
        format_split = parseo.split(sep='.')
        
        request.data['name_img'] = parseo
        request.data['format_img'] = format_split[1]
        
        serializer = TablaImg(data=request.data, context ={'request':request })
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewDetailImg(APIView):
    def get_object(self, pk):
        try:
            return ImgModel.objects.get(pk=pk)
        except ImgModel.DoesNotExist:
            return 404

    def delete(self, request, pk, format=None):
        idResponse = self.get_object(pk)
        if idResponse != 404:
            idResponse.img.delete()
            idResponse.delete()
        else:
            return Response('Id no encontrada')  
        
class ResponseCustom():
    #def response_custom(delf, )
    ...