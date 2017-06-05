# -*- coding: utf-8 -*-

from django.contrib import admin
from agenda.models import Pessoa, Telefone, Email, Cadastro


class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome')


class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('numero', 'tipo')


class EmailAdmin(admin.ModelAdmin):
    list_display = ('endereco', 'tipo')


class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'pai', 'mae', 'data_nascimento', 'endereco', 'email_pessoal', 'email_institucional', 'telefone_residencial', 'telefone_celular')


admin.site.register(Pessoa)
admin.site.register(Telefone, TelefoneAdmin)
admin.site.register(Email, EmailAdmin)
admin.site.register(Cadastro, CadastroAdmin)
