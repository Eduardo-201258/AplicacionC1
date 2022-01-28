from rest_framework import serializers

#Importacion de modelos
from register.models import RegisterUsers

class TablaUsers(serializers.ModelSerializer):
    class Meta:
        model = RegisterUsers
        fields = (  "usuario", "correo", "contraseña")