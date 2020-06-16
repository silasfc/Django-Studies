from django.contrib import admin
from django.conf.locale.pt_BR import formats as pt_BR_formats
pt_BR_formats.DATE_FORMAT = "d/m/Y"
from .models import *


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome',)


@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'cpf')


@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'razao_social', 'cnpj')


@admin.register(Cor)
class CorAdmin(admin.ModelAdmin):
    pass


@admin.register(FabricanteVeiculo)
class FabricanteVeiculoAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoriaVeiculo)
class CategoriaVeiculoAdmin(admin.ModelAdmin):
    pass


@admin.register(ModeloVeiculo)
class ModeloVeiculoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'fabricante', 'categoria')


@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'ano_fabricao', 'ano_modelo', 'cor')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    filter_horizontal = ('veiculos',)
    list_display = ('pessoa',)


@admin.register(TipoEndereco)
class TipoEnderecoAdmin(admin.ModelAdmin):
    pass


@admin.register(Endereco)
class EnderecoAdmin(admin.ModelAdmin):
    list_display = ('logradouro', 'cep')


@admin.register(TipoTelefone)
class TipoTelefoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ('ddd', 'numero')


@admin.register(TipoEmail)
class TipoEmailAdmin(admin.ModelAdmin):
    pass


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('endereco',)


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    filter_horizontal = ('endereco', 'telefone', 'email')


@admin.register(Revisao)
class RevisaoAdmin(admin.ModelAdmin):
    list_display = ('ordem_servico', 'veiculo', 'oficina', 'data', 'rodagem', 'custo')
    exclude = ('numero', 'ano', 'ordem_servico')
    readonly_fields = ('custo',)


@admin.register(FabricantePeca)
class FabricantePecaAdmin(admin.ModelAdmin):
    pass


@admin.register(CategoriaPeca)
class CategoriaPecaAdmin(admin.ModelAdmin):
    pass


@admin.register(ModeloPeca)
class ModeloPecaAdmin(admin.ModelAdmin):
    pass


@admin.register(Peca)
class PecaAdmin(admin.ModelAdmin):
    list_display = ('revisao', 'descricao', 'custo', 'descricao')


@admin.register(TipoServico)
class TipoServicoAdmin(admin.ModelAdmin):
    pass


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('revisao', 'oficina', 'custo', 'descricao')


@admin.register(Oficina)
class OficinaAdmin(admin.ModelAdmin):
    pass


@admin.register(ItemCheckup)
class ItemCheckupAdmin(admin.ModelAdmin):
    pass


@admin.register(Checkup)
class CheckupAdmin(admin.ModelAdmin):
    list_display = ('veiculo', 'data', 'rodagem', 'observacoes')
