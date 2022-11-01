from django.shortcuts import render
from rest_framework.viewsets import *

from home.models import Endereco,Cliente, Conta,Cartao,Fatura,Transacao,Emprestimo,Pag_emprestimo,Favoritos,Extrato
from home.serializers import EnderecoSerializer,ClienteSerlializer,ContaSerializer,CartaoSerializer,FaturaSerializer,TransacaoSerializer,EmprestimoSerializer,PagEmprestimoSerialzer,FavoritoSerializer,ExtratoSerializer


class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerlializer

class EnderecoViewSet(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

class ContaViewSet(ModelViewSet):
    queryset = Conta.objects.all()
    serializer_class = ContaSerializer

class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer 

class FaturaViewSet(ModelViewSet):
    queryset = Fatura.objects.all()
    serializer_class = FaturaSerializer 

class TransacaoViewSet(ModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer 

class EmprestimoViewSet(ModelViewSet):
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer 

class PagEmprestimoViewSet(ModelViewSet):
    queryset = Pag_emprestimo.objects.all()
    serializer_class = PagEmprestimoSerialzer 

class FavoritosViewSet(ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritoSerializer 

class ExtratoViewSet(ModelViewSet):
    queryset = Extrato.objects.all()
    serializer_class = ExtratoSerializer 

