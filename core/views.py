from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.decorators import detail_route, api_view

from .serializers import UserSerializer, ProgramaSerializer
from .models import Programa

class ProgramaViewSet(viewsets.ModelViewSet):

    queryset = Programa.objects.all()
    serializer_class = ProgramaSerializer

    def list(self, request):
        queryset = Programa.objects.all()
        serializer = ProgramaSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Programa.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProgramaSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        if request.method == 'POST':
            serializer = ProgramaSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if request.method == 'PUT':
            serializer = ProgramaSerializer(request.user, data=request.DATA, partial=True)
        return super(ProgramaViewSet, self).update(request)

    def destroy(self, request, pk=None):
        if request.method == 'DELETE':
            serializer = ProgramaSerializer(data=request.DATA)

        return super(ProgramaViewSet, self).destroy(request)