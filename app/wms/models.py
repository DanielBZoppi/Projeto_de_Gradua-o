from django.db import models

class Produto(models.Model):
    hora_entrada = models.TimeField()
    data_entrada = models.DateField()
    nome = models.CharField(max_length=100)
    produto_id = models.CharField(max_length=50, unique=True)
    quantidade = models.PositiveIntegerField()
    empresa = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nome} ({self.produto_id})"