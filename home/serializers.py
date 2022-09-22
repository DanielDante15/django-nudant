from rest_framework.serializers import ModelSerializer

from .models import *


class ClienteSerlializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nome', 'email', 'cpf', 'contato', 'endereco')


class EnderecoSerializer(ModelSerializer):
    class Meta:
        model = Endereco
        fields = ('cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'num_casa')


class ContaSerializer(ModelSerializer):
    class Meta:
        model = Conta
        fields = ('saldo', 'cliente', 'agencia', 'conta', 'tipo_de_conta')


class CartaoSerializer(ModelSerializer):
    class Meta:
        model = Cartao
        fields = ('saldo', 'cliente', 'agencia', 'conta', 'tipo_de_conta')


class FaturaSerializer(ModelSerializer):
    class Meta:
        model = Fatura
        fields = ('cartao', 'valor_fatura', 'data_vencimento', 'data_pagamento')


class TransacaoSerializer(ModelSerializer):
    class Meta:
        model = Transacao
        fields = ('beneficiario', 'beneficiado', 'data_transacao', 'valor_transacao')


class EmprestimoSerializer(ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = ('status', 'conta', 'valor', 'data', 'juros', 'parcelas')


class PagEmprestimoSerialzer(ModelSerializer):
    class Meta:
        model = Pag_emprestimo
        fields = ('emprestimo', 'data_vencimento', 'valor_parcela', 'data_pagamento')


class FavoritoSerializer(ModelSerializer):
    class Meta:
        model = Favoritos
        fields = ('usuario', 'ctt_favorito')


class ExtratoSerializer(ModelSerializer):
    class Meta:
        model = Extrato
        fields = ('conta', 'operacao', 'data', 'valor')
