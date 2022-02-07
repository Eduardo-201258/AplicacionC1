from wsgiref import validate
from rest_framework import serializers

# importarcion de modelos 
from register.models import RegisterUsers

class TablaUsers(serializers.ModelSerializer):
    class Meta:
        model = RegisterUsers
        fields = ('user','email','password')    
