from pyexpat import model
from rest_framework import serializers
from processos import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'processo', 'data', 'start_hour', 'end_hour', 'situacao', 'observacoes')
