from django.db import models
from datetime import date


class Comum(models.Model):
    '''docstring for Comum'''
    nome = models.CharField(max_length=64)

    class Meta:
        verbose_name = "Comum"
        verbose_name_plural = "Comuns"

    def __str__(self):
        return self.nome


class Pessoa(Comum):
    '''docstring for Pessoa'''

    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'


class PessoaFisica(Pessoa):
    '''docstring for PessoaFisica'''

    sobrenome = models.CharField(max_length=96)
    cpf = models.CharField(max_length=11, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'

    def __str__(self):
        return (self.nome + ' ' + self.sobrenome)


class PessoaJuridica(Pessoa):
    '''docstring for PessoaJuridica'''

    razao_social = models.CharField(max_length=96)
    cnpj = models.CharField(max_length=14, blank=True, null=True, unique=True)

    class Meta:
        verbose_name = 'Pessoa Jurídica'
        verbose_name_plural = 'Pessoas Jurídicas'

    def __str__(self):
        return (self.nome + ' - ' + self.razao_social)


class Cor(Comum):

    class Meta:
        verbose_name = "Cor"
        verbose_name_plural = "Cores"


class FabricanteVeiculo(Comum):

    class Meta:
        verbose_name = "Fabricante de Veículo"
        verbose_name_plural = "Fabricante de Veículos"


class CategoriaVeiculo(Comum):
    '''docstring for CategoriaVeiculo'''

    class Meta:
        verbose_name = "Categoria de Veículo"
        verbose_name_plural = "Categoria de Veículos"


class ModeloVeiculo(Comum):
    '''docstring for ModeloVeiculo'''

    fabricante = models.ForeignKey(FabricanteVeiculo, related_name='modelosveiculos')
    categoria = models.ForeignKey(CategoriaVeiculo, related_name='modelosveiculos')

    class Meta:
        verbose_name = "Modelo de Veículo"
        verbose_name_plural = "Modelo de Veículos"

    def __str__(self):
        return (self.nome + str(self.fabricante))


class Veiculo(models.Model):
    '''docstring for Veiculo'''

    placa = models.CharField(max_length=7, unique=True)
    modelo = models.ForeignKey(ModeloVeiculo, related_name='veiculo')
    ano_fabricao = models.PositiveSmallIntegerField(blank=True, null=True)
    ano_modelo = models.PositiveSmallIntegerField(blank=True, null=True)
    cor = models.ForeignKey(Cor, related_name='veiculos')
    descricao = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"

    def __str__(self):
        return (str(self.modelo) + ' - ' + self.placa)


class Cliente(models.Model):
    '''docstring for Cliente'''

    pessoa = models.ForeignKey(Pessoa, related_name='clientes')
    veiculos = models.ManyToManyField(Veiculo, related_name='clientes')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome


class TipoEndereco(Comum):
    ''' docstring for TipoEndereco '''

    class Meta:
        verbose_name = "Tipo de Endereço"
        verbose_name_plural = "Tipos de Endereços"


class Endereco(models.Model):
    ''' docstring for Endereco '''

    tipo = models.ForeignKey(TipoEndereco, related_name='enderecos')
    logradouro = models.CharField(max_length=128)
    cep = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return (self.tipo + ' - ' + self.logradouro)


class TipoTelefone(Comum):
    ''' docstring for TipoTelefone '''

    class Meta:
        verbose_name = "Tipo de Telefone"
        verbose_name_plural = "Tipos de Telefones"


class Telefone(models.Model):
    ''' docstring for Telefone '''

    tipo = models.ForeignKey(TipoTelefone, related_name='telefones')
    ddd = models.CharField(max_length=2)
    numero = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Telefone'
        verbose_name_plural = 'Telefones'

    def __str__(self):
        return ('('+self.ddd+')' + ' ' + self.numero)


class TipoEmail(Comum):
    ''' docstring for TipoEmail '''
    class Meta:
        verbose_name = "Tipo de Email"
        verbose_name_plural = "Tipos de Emails"


class Email(models.Model):
    '''docstring for Email'''

    tipo = models.ForeignKey(TipoEmail, related_name='emails')
    endereco = models.EmailField(max_length=64)

    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emails'

    def __str__(self):
        return (self.tipo + ' - ' + self.endereco)


class Contato(models.Model):
    ''' docstring for Contato '''

    responsavel = models.ForeignKey(Pessoa, related_name='contatos')
    endereco = models.ManyToManyField(Endereco, related_name='contatos')
    telefone = models.ManyToManyField(Telefone, related_name='contatos')
    email = models.ManyToManyField(Email, related_name='contatos')

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return self.responsavel.nome


class Oficina(PessoaJuridica):
    ''' docstring for Oficina '''

    class Meta:
        verbose_name = 'Oficina'
        verbose_name_plural = 'Oficinas'

    def __str__(self):
        return self.nome


class Revisao(models.Model):
    ''' docstring for Revisao '''

    numero = models.SmallIntegerField(null=True)
    ano = models.SmallIntegerField(null=True)
    ordem_servico = models.CharField(max_length=10, null=True, db_index=True)
    veiculo = models.ForeignKey(Veiculo, related_name='revisoes')
    oficina = models.ForeignKey(Oficina, related_name='revisoes')
    data = models.DateField()
    rodagem = models.PositiveIntegerField()
    custo = models.FloatField(null=True, default=0)

    class Meta:
        verbose_name = 'Revisão'
        verbose_name_plural = 'Revisões'

    def save(self, *args, **kwargs):
        self.custo = self.calc_custo

        if not self.numero:
            self.ano = self.ano if self.ano else date.today().year
            self.numero = self.proximo_numero
        self.ordem_servico = '%04d/%d' % (self.numero, self.ano)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.ordem_servico

    @property
    def proximo_numero(self):
        query = self.__class__.objects.filter(
            ano=self.ano
        ).order_by(
            'numero'
        ).aggregate(
            numero_max=models.Max('numero')
        )

        return int(query.get('numero_max') or 0) + 1

    @property
    def calc_custo(self):
        query_pecas = self.pecas.filter().aggregate(models.Sum('custo'))
        query_servicos = self.servicos.filter().aggregate(models.Sum('custo'))

        return (query_pecas.get('custo__sum') or 0) + (query_servicos.get('custo__sum') or 0)


class FabricantePeca(Comum):

    class Meta:
        verbose_name = "Fabricante de Peça"
        verbose_name_plural = "Fabricantes de Peças"


class CategoriaPeca(Comum):

    class Meta:
        verbose_name = "Categoria de Peça"
        verbose_name_plural = "Categorias de Peças"


class ModeloPeca(Comum):
    fabricante = models.ForeignKey(FabricantePeca, related_name='modelospecas')
    categoria = models.ForeignKey(CategoriaPeca, related_name='modelospecas')

    class Meta:
        verbose_name = "Modelo de Peça"
        verbose_name_plural = "Modelos de Peças"


class Peca(models.Model):
    ''' docstring for Peca '''

    revisao = models.ForeignKey(Revisao, related_name='pecas')
    modelo = models.ForeignKey(ModeloPeca, related_name='peca')
    custo = models.FloatField()
    descricao = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = 'Peça'
        verbose_name_plural = 'Peças'

    def __str__(self):
        return (self.modelo + ' - ' + self.fabricante + ' - ' + 'R$' + str(self.custo))


class TipoServico(Comum):
    ''' docstring for TipoServico '''

    class Meta:
        verbose_name = "Tipo de Serviço"
        verbose_name_plural = "Tipos de Serviços"


class Servico(models.Model):
    ''' docstring for Servico '''

    revisao = models.ForeignKey(Revisao, related_name='servicos')
    oficina = models.ForeignKey(Oficina, related_name='servicos')
    mecanico = models.ForeignKey(PessoaFisica, related_name='servicos')
    tipo = models.ForeignKey(TipoServico, related_name='servicos')
    custo = models.FloatField()
    descricao = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return (self.tipo + ' ' + str(self.custo))


class ItemCheckup(Comum):
    ''' docstring for ItemCheckup '''

    class Meta:
        verbose_name = "Item de Checkup"
        verbose_name_plural = "Itens de Checkups"


class Checkup(models.Model):
    ''' docstring for Checkup de rotina '''

    veiculo = models.ForeignKey(Veiculo, related_name='manutencoes')
    item = models.ForeignKey(ItemCheckup, related_name='checkups')
    data = models.DateField()
    rodagem = models.PositiveIntegerField()
    observacoes = models.TextField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = 'Checkup'
        verbose_name_plural = 'Checkups'

    def __str__(self):
        return (self.data.strftime('%d/%m/%Y') + ' - ' + self.get_item_display())
