from django.db import models
from django.db.models import *


class Endereco(models.Model):
    cep = models.CharField(max_length=8, verbose_name='CEP')
    logradouro = models.CharField(max_length=30, verbose_name="Logradouro")
    complemento = models.CharField(max_length=30, verbose_name="Compemento")
    bairro = models.CharField(max_length=30, verbose_name="Bairro")
    localidade = models.CharField(max_length=20, verbose_name="Localidade")
    uf = models.CharField(max_length=20, verbose_name="UF")
    num_casa = models.SmallIntegerField(verbose_name="Número")

    def __str__(self):
        return self.logradouro


class Cliente(models.Model):

    GEN_MASCULINO = 'M'
    GEN_FEMININO = 'F'

    GEN = [
        (GEN_FEMININO,'Feminino'),
        (GEN_MASCULINO,'Masculino'),
    ]

    nome = models.CharField(max_length=50, verbose_name="Nome")
    email = models.EmailField(verbose_name="email")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    contato = models.CharField(max_length=10, verbose_name="Contato")
    endereco = models.ForeignKey(Endereco, on_delete=models.CASCADE, verbose_name="Endereço")

    def __str__(self):
        return self.nome


class Conta(models.Model):
    CONTA_CORRENTE = 'CC'
    CONTA_POUPANCA = 'CP'
    CONTA_SALARIO = 'CS'

    TIPO_CONTA = [
        (CONTA_POUPANCA, 'Conta Poupança'),
        (CONTA_CORRENTE, 'Conta Corrente'),
        (CONTA_SALARIO, 'Conta Salario')
    ]

    saldo = models.DecimalField(max_digits=11, decimal_places=2, verbose_name="Saldo")
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name="Cliente")
    agencia = models.CharField(max_length=5, verbose_name="Agencia")
    conta = models.CharField(max_length=20, verbose_name="Conta")
    tipo_de_conta = models.CharField(max_length=2, choices=TIPO_CONTA,default=CONTA_CORRENTE, verbose_name='Tipo de conta')

    def __str__(self):
        return self.conta


class Cartao(models.Model):
    BANDEIRA_VISA = 'Visa'
    BANDEIRA_MASTERCARD = 'Mastercard'
    BANDEIRA_ELO = 'Elo'

    BANDEIRA = [
        (BANDEIRA_MASTERCARD, 'MasterCard'),
        (BANDEIRA_ELO, 'Elo'),
        (BANDEIRA_VISA, 'Visa'),
    ]

    cvv = models.SmallIntegerField(verbose_name="Código de verificação")
    validade = DateField(verbose_name="Data de validade")
    vencimento = PositiveSmallIntegerField(verbose_name="Dia do vencimento")
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, verbose_name="Conta")
    bandeira = models.CharField(max_length=10, choices=BANDEIRA,default=BANDEIRA_VISA, verbose_name="Bandeira")
    limite = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Limite")

    def __str__(self):
        return str(self.bandeira) + " - " + str(self.limite)


class Fatura(Model):
    cartao = ForeignKey(Cartao, on_delete=CASCADE, verbose_name="Cartão")
    valor_fatura = DecimalField(max_digits=8, decimal_places=2)
    data_vencimento = DateField(verbose_name="Vencimento")
    data_pagamento = DateField(verbose_name="Pagamento")

    def __str__(self):
        return self.data_vencimento


class Transacao(models.Model):
    beneficiario = ForeignKey(Conta, on_delete=CASCADE, verbose_name="Beneficiário", related_name='beneficiario')
    beneficiado = ForeignKey(Conta, on_delete=CASCADE, verbose_name="Beneficiado", related_name='beneficiado')
    data_transacao = DateTimeField(verbose_name='Data', auto_now_add=True)
    valor_transacao = DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return self.beneficiario + " " + self.beneficiado


class Emprestimo(Model):
    STATUS_DIA = 'D'
    STATUS_ATRASADO = 'A'

    STATUS = [(STATUS_DIA, 'Em dia'),(STATUS_ATRASADO, 'Em atraso'),]

    status = CharField(max_length=1, choices=STATUS, default=STATUS_DIA, verbose_name="Status")
    conta = ForeignKey(Conta, on_delete=CASCADE, verbose_name="Conta")
    valor = DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor do empréstimo")
    data = DateTimeField(verbose_name="Data", auto_now_add=True)
    juros = DecimalField(max_digits=4, decimal_places=2, verbose_name="Juros")
    parcelas = SmallIntegerField()

    def __str__(self):
        return str(self.conta)

class Pag_emprestimo(Model):

    emprestimo = ForeignKey(Emprestimo, on_delete=CASCADE, verbose_name="Emprestimo")
    data_vencimento = DateField(verbose_name="Data de vencimento")
    valor_parcela = DecimalField(max_digits=8, decimal_places=2, verbose_name="Valor da parcela")
    data_pagamento = DateField(verbose_name="Data de pagamento")

    def __str__(self):
        return str(self.emprestimo)


class Favoritos(Model):
    usuario = ForeignKey(Cliente, on_delete=CASCADE, verbose_name="Usuário", related_name="usuario")
    ctt_favorito = ForeignKey(Cliente, on_delete=CASCADE, verbose_name="Favorito", related_name="favorito")

    def __str__(self):
        return self.usuario

class Extrato(Model):
    OP_SAIDA = 'S'
    OP_ENTRADA = 'E'

    OPERACAO = [
        (OP_ENTRADA, 'Entrada'),
        (OP_SAIDA, 'Saída')
    ]

    conta = ForeignKey(Conta, on_delete=CASCADE, verbose_name="Conta")
    operacao = CharField(max_length=1, choices=OPERACAO,default=OP_ENTRADA, verbose_name="Operação")
    data = DateTimeField(auto_now_add=True, verbose_name="Data")
    valor = DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")

    def __str__(self):
        return self.conta
