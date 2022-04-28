from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import FileSerializer
from .models import File

# Create your views here.


class FileViewSet(ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()
