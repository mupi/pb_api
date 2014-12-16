from django.shortcuts import render
from rest_framework import generics
from .models import Associado
from .serializers import AssociadoSerializer

class AssociadoListView(generics.ListAPIView):
    queryset = Associado.objects.all()
    serializer_class = AssociadoSerializer


