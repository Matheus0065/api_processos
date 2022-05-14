from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from api import models


class APISerializer(serializers.ModelSerializer):
    class Meta:
        model = models.API
        fields = ('id', 'processo', 'data', 'start_hour', 'end_hour', 'situacao', 'observacoes')
