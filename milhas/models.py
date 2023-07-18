from django.db import models
import random

class Depoimento(models.Model):
    foto = models.ImageField(upload_to='depoimentos', null=True, blank=True)
    depoimento = models.TextField(null=True, blank=True)
    autor = models.CharField(max_length=75, null=True, blank=True)

    def __str__(self):
        return self.autor
