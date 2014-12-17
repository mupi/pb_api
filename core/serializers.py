from rest_framework import serializers
from .models import Associado, Programa

class AssociadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Associado
        fields = ('id', 'nome_instituicao', 'matricula')

class ProgramaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Programa
        fields = ('id', 'titulo')
