from django.urls import is_valid_path
from rest_framework.response import Response
from register.models import RegisterUsers
from register.serializers import TablaUsers
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = RegisterUsers.objects.all()
        serializer = TablaUsers(queryset, many=True, context={'request':request})
        return Response(serializer.data)
        
    def post(self, request, format=None):
        serializer = TablaUsers(data=request.data, context ={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)