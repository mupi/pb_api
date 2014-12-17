from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from rest_framework import generics

from .models import Associado, Programa
from .serializers import AssociadoSerializer, ProgramaSerializer

class AssociadoListView(generics.ListAPIView):
    queryset = Associado.objects.all()
    serializer_class = AssociadoSerializer;

class ProgramaListView(generics.ListAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer;

class ProgramaDetailView(generics.RetrieveAPIView):
    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

class ProgramaForm(ModelForm):
    class Meta:
        model = Programa

def programa_list(request, template_name='core/programa_list.html'):
    programas = Programa.objects.all()
    data = {}
    data['object_list'] = programas
    return render(request, template_name, data)

def programa_create(request, template_name='core/form.html'):
    form = ProgramaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('programa_list')
    return render(request, template_name, {'form':form})

def programa_update(request, pk, template_name='core/form.html'):
    programa = get_object_or_404(Programa, pk=pk)
    form = ProgramaForm(request.POST or None, instance=programa)
    if form.is_valid():
        form.save()
        return redirect('programa_list')
    return render(request, template_name, {'form':form})

def programa_delete(request, pk, template_name='core/confirm_delete.html'):
    programa = get_object_or_404(Programa, pk=pk)    
    if request.method=='POST':
        programa.delete()
        return redirect('programa_list')
    return render(request, template_name, {'object':programa})
