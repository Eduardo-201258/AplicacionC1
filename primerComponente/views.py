from rest_framework.views import APIView
from rest_framework.response import Response
from aplicacionC1.primerComponente import serializers

from primerComponente.models import PrimerModelo
from primerComponente.serializers import PrimerTablaSerializer

# Create your views here.
class PrimerViewList(APIView):
    def get(self, request, format=None):
        queryset = PrimerModelo.objects.all()
        serializer = PrimerTablaSerializer(queryset, many=True, context={'request':request})
        return Response(serializer.data)
