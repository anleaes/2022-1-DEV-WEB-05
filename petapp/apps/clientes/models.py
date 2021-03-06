from django.db import models

# Create your models here.

class Cliente(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    nome = models.CharField('Nome', max_length=50)
    endereco = models.TextField('Endereco', max_length=100) 
    cpf = models.IntegerField('Cpf',null=True, blank=True,default=0)
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

    def __str__(self):
        return self.nome