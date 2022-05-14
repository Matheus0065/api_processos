from django.db import models

# Create your models here.

class Task(models.Model):
    processo = models.CharField(max_length=255)
    data = models.DateField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    situacao = models.CharField(max_length=50)
    observacoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.processo} ({self.id})"
