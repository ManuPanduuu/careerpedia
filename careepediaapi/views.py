from django.shortcuts import render
from rest_framework import viewsets
from .models import Bachelor, Intermediate
from .serializers import BachelorsSerializers, IntermediateSerializers


class BachelorViewSet(viewsets.ModelViewSet):
    queryset = Bachelor.objects.all()
    serializer_class = BachelorsSerializers


class IntermediateViewSet(viewsets.ModelViewSet):
    queryset = Intermediate.objects.all()
    serializer_class = IntermediateSerializers
