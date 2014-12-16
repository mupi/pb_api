from rest_framework import serializers
from .models import Associado

class AssociadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Associado
        fields = ('id', 'nome_instituicao', 'matricula')
