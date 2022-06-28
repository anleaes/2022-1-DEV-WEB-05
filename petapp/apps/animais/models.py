from django.db import models
from clientes.models import Cliente

# Create your models here.

class Animal(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    nome = models.CharField('Nome', max_length=50)
    peso = models.TextField('Peso', max_length=10)
    raca = models.CharField('raca', max_length=20)
    photo = models.ImageField('Foto', upload_to='photos')
    doc = models.FileField('Documentos', upload_to='docs')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    #cliente = models.ManyToManyField(Cliente, through='Cliente', blank=True)
    
    class Meta:
        verbose_name = 'Animal'
        verbose_name_plural = 'Animais'
        ordering =['id']

    def __str__(self):
        return self.nome