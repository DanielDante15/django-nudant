from django.contrib import admin

from .models import Conta,Cliente,Emprestimo,Endereco,Cartao, Fatura,Transacao,Pag_emprestimo,Favoritos,Extrato


admin.site.register(Conta)
admin.site.register(Cliente)
admin.site.register(Emprestimo)
admin.site.register(Endereco)
admin.site.register(Cartao)
admin.site.register(Fatura)
admin.site.register(Transacao)
admin.site.register(Pag_emprestimo)
admin.site.register(Favoritos)
admin.site.register(Extrato)

# Register your models here.
