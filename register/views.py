from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from register.models import RegisterUsers
from register.serializers import TablaUsers

# Create your views here.
class RegisterView(ObtainAuthToken):
    def put(self, request, *args, **kwargs):
        data = RegisterUsers.objects.all()
        serializer = TablaUsers(data, many=True, context={'request':request})
        user=serializer.validated_data['user']
        token,create=Token.objects.get_or_create(user=user)
        return Response(
            {
            'token':token.key,
            'usuario':data.usuario,
            'correo':data.correo,
            }
        )
        
