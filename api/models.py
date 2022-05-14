import uuid
from django.db import models
from uuid import uuid4

# Create your models here.

class API(models.Model):
    processo = models.CharField(max_length=255)
    data = models.DateField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    situacao = models.CharField(max_length=50)
    observacoes = models.TextField(null=True, blank=True)
