from django.db import models

# Create your models here.

class Tipo(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    nome = models.CharField('Nome', max_length=50)
    descricao = models.TextField('Descricao', max_length=100) 
    
    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'
        ordering =['id']

    def __str__(self):
        return self.nome