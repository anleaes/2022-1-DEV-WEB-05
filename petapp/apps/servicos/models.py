from django.db import models
from tipos.models import Tipo

class Servico(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    descricao = models.TextField('Descricao', max_length=100)
    valor = models.FloatField('valor', null=True, blank=True, default=0.0)
    tempoexecucao = models.IntegerField('Tempo execucao',null=True, blank=True,default=0)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'
        ordering =['id']

    def __str__(self):
        return self.descricao