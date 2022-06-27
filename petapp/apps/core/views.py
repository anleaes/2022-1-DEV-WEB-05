from django.shortcuts import render
from animais.models import Animal

# Create your views here.

def home(request):
    template_name = 'animais/list_animais.html'
    animais = Animal.objects.filter()
    context = {
        'animais': animais
    }
    return render(request, template_name, context)