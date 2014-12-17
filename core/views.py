from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, status
from rest_framework.response import Response

from .serializers import UserSerializer

from django.contrib.auth.models import User

class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = User.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def create(self, request):
        if request.method == 'POST':
	        serializer = UserSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if request.method == 'PUT':
	        serializer = UserSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        if request.method == 'DELETE':
	        serializer = UserSerializer(data=request.DATA)

        if serializer.is_valid():
            serializer.delete()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)