from dataclasses import field
from rest_framework import serializers

#Importacion de modelos
from loadImage.models import ImgModel

class TablaImg(serializers.ModelSerializer):
    class Meta:
        model = ImgModel
        fields = ("name_img", "url_img", "format_img" )
