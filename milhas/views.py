from django.shortcuts import render
from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from milhas.models import Depoimento
from milhas.serializer import DepoimentoSerializer


class DepoimentosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os depoimentos"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
