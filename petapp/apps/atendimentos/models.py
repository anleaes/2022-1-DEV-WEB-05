from django.db import models
from animais.models import Animal
from servicos.models import Servico 

# Create your models here.

class Atendimento(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('codigo', max_length=50)
    description = models.TextField('Descricao', max_length=100)
    date_fabrication = models.DateField('Data', auto_now=False, auto_now_add=False) 
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    atendimento_servico = models.ManyToManyField(Servico, through='AtendimentoServico', blank=True)
    
    class Meta:
        verbose_name = 'Atendimento'
        verbose_name_plural = 'Atendimentos'
        ordering =['id']

    def __str__(self):
        return self.name

class AtendimentoServico(models.Model):
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Itens de Servico'
        verbose_name_plural = 'Itens de Servicos '
        ordering =['id']

    def __str__(self):
        return self.servico.descricao
