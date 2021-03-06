from django.shortcuts import render, get_object_or_404, redirect
from .forms import TipoForm
from .models import Tipo

# Create your views here.

def add_tipo(request):
    template_name = 'tipos/add_tipo.html'
    context = {}
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tipos:list_tipos')
    form = TipoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tipos(request):
    template_name = 'tipos/list_tipos.html'
    tipos = Tipo.objects.filter()
    context = {
        'tipos': tipos
    }
    return render(request, template_name, context)

def edit_tipo(request, id_tipo):
    template_name = 'tipos/add_tipo.html'
    context ={}
    tipo = get_object_or_404(Tipo, id=id_tipo)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('tipos:list_tipos')
    form = TipoForm(instance=tipo)
    context['form'] = form
    return render(request, template_name, context)

def delete_tipo(request, id_tipo):
    tipo = Tipo.objects.get(id=id_tipo)
    tipo.delete()
    return redirect('tipos:list_tipos')