from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    idade = models.BigIntegerField()
    pais = models.CharField(max_length=30)
    
