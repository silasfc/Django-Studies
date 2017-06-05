# -*- coding: utf-8 -*-
from django.contrib import admin
from sigesti.models import AreaResponsavel, Lotacao, Categoria, Status, Equipamento, Emprestimo, Usuario, Assentamento, SLA, AssistenciaTecnica, Endereco, Solucao, Problema, Garantia, Chamado, AtendimentoExterno


@admin.register(AreaResponsavel)
class AreaResponsavelAdmin(admin.ModelAdmin):
    pass
    # list_display = ('descricao',)


@admin.register(Lotacao)
class LotacaoAdmin(admin.ModelAdmin):
    pass
    list_display = ('sigla', 'nome')


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # pass
    # list_display = ('descricao',)
    filter_horizontal = ('equipamentos',)
    # filter_vertical = ('equipamentos',)
    # raw_id_fields = ['equipamentos']  #  campo p/ o id do objeto relacionado
    # radio_fields = {"descricao": admin.VERTICAL}
    # radio_fields = {"descricao": admin.HORIZONTAL}
    pass

@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    pass
    # list_display = ('descricao', 'patrimonio', 'numero_serie', 'observacao', 'fabricante', 'modelo', 'data_cadastro', 'disponibilidade')  # , 'categoria'


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    pass
    # list_display = ('justificativa', 'data_emprestimo', 'data_devolucao', 'data_limite', 'observacao', 'responsavel', 'solicitante', 'equipamento')


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass
    # list_display = ('nome', 'sobrenome', 'login', 'matricula', 'senha', 'email', 'nivel', 'data_cadastro', 'area_responsavel', 'lotacao')


@admin.register(SLA)
class SLAAdmin(admin.ModelAdmin):
    pass
    # list_display = ('descricao', 'tempo')


@admin.register(AssistenciaTecnica)
class AssistenciaTecnicaAdmin(admin.ModelAdmin):
    pass
    # list_display = ('razao_social', 'nome_fantasia', 'cnpj', 'contato', 'responsavel', 'email', 'fax', 'site')


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    pass
    list_display = ('logradouro', 'cidade', 'uf', 'cep', 'assistencia_tecnica')


@admin.register(Solucao)
class SolucaoAdmin(admin.ModelAdmin):
    pass
    # list_display = ('descricao',)


@admin.register(Problema)
class ProblemaAdmin(admin.ModelAdmin):
    pass
    # list_display = ('descricao', 'possivel_causa', 'area_responsavel', 'sla')  # , 'solucao'


@admin.register(Garantia)
class GarantiaAdmin(admin.ModelAdmin):
    pass
    # list_display = ('descricao', 'detalhes')


@admin.register(Chamado)
class ChamadoAdmin(admin.ModelAdmin):
    pass
    # list_display = ('desc_chamado', 'data_abertura', 'data_encerramento', 'desc_problema', 'desc_solucao', 'area_responsavel', 'equipamento', 'usuario')  # 'operador', 'problema',


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass
    # list_display = ('data_inicial', 'data_final', 'chamado', 'descricao')


@admin.register(Assentamento)
class AssentamentoAdmin(admin.ModelAdmin):
    pass
    # list_display = ('descricao', 'chamado')


@admin.register(AtendimentoExterno)
class AtendimentoExternoAdmin(admin.ModelAdmin):
    pass
    # list_display = ('descricao', 'data_saida', 'data_retorno', 'custo', 'chamado', 'garantia')  # 'assistencia_tecnica',
