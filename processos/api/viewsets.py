from rest_framework import viewsets
from processos.api import serializers
from processos import models


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskSerializer
    queryset = models.Task.objects.all()
