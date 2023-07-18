import random
from rest_framework import viewsets
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

class DepoimentosHomeViewSet(viewsets.ModelViewSet):
    """Exibindo tres depoimentos aleatorios"""
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        depoimentos = Depoimento.objects.all()
        queryset = random.sample(list(depoimentos), k=3)
        return queryset