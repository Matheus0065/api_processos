from rest_framework import viewsets
from api.api import serializers
from api import models


class APIViewSet(viewsets.ModelViewSet):
    serializer_class =  serializers.APISerializer
    queryset = models.API.objects.all()
