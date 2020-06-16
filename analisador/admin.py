from django.contrib import admin
from django.conf.locale.pt_BR import formats as pt_BR_formats
from analisador.models import Acao, Dado, Analise
pt_BR_formats.DATE_FORMAT = "d/m/Y"


@admin.register(Acao)
class AcaoAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'abreviatura')
    # list_editable = ('nome_fantasia', 'abreviatura')
    list_filter = ('nome_fantasia',)


@admin.register(Dado)
class DadoAdmin(admin.ModelAdmin):
    fields = ('acao', 'data', 'valor_fechamento', 'vpa', 'vpa_p_bm', 'mma', 'mme', 'correlacao')
    readonly_fields = ('vpa_p_bm', 'mma', 'mme', 'correlacao')
    list_display = ('data', 'acao', 'valor_fechamento', 'vpa', 'vpa_p_bm', 'mma', 'mme', 'correlacao')
    list_filter = ('acao', 'data')
    search_fields = ('acao__nome_fantasia', 'data', 'valor_fechamento', 'vpa', 'vpa_p_bm', 'mma', 'mme')
    list_per_page = 100
    # list_max_show_all = 300
    list_select_related = ('acao',)


# ordinal.short_description = 'Testando...'


@admin.register(Analise)
class Analise(admin.ModelAdmin):
    list_display = ('data', 'ordinal', 'dado', 'decisao')
    fields = ('data', 'ordem', 'dado', 'decisao')
    readonly_fields = ('data', 'ordem', 'dado', 'decisao')
    # list_display_links = None
    list_filter = ('data', 'ordem', 'decisao')
    search_fields = ('data', 'ordem', 'decisao')
    # actions = [ordinal]
