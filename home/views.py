import decimal
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
    
    def create(self, request, *args, **kwargs):

        beneficiario = Conta.objects.get(pk=self.request.data["beneficiario"])
        beneficiado = Conta.objects.get(pk=self.request.data["beneficiado"])
        valor = decimal.Decimal(self.request.data["valor_transacao"])

        if beneficiario.saldo >= valor:

            enviador = {'cliente':beneficiario.pk,'conta':beneficiario.conta,'agencia':beneficiario.agencia,'saldo':beneficiario.saldo-valor}
            serializer = ContaSerializer(beneficiario, data=enviador)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)

            recebedor = {'cliente':beneficiado.pk,'agencia':beneficiado.agencia,'conta':beneficiado.conta,'saldo':beneficiado.saldo+valor}

            serializer_dois = ContaSerializer(beneficiado,data=recebedor)
            if serializer_dois.is_valid():
                serializer_dois.save()

            else:
                print(serializer.errors)

        return super().create(request,*args,**kwargs)


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

