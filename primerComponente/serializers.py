from rest_framework import serializers

#Importacion de modelos
from primerComponente.models import PrimerModelo

class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerModelo
        fields = (  "campo_uno", "edad")