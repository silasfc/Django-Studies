# -*- coding: utf-8 -*-

from datetime import datetime
from django.db import models


class AreaResponsavel(models.Model):
    """
    Área responsável por atender a demanda
    """

    DESCRICAO_CHOICES = (
        (1, 'Help Desk e Manutenção'),
        (2, 'Redes e Segurança da Informação'),
        (3, 'Desenvolvimento e Banco de Dados'),
        (4, 'Diretoria de Tecnologia da Informação')
    )

    descricao = models.SmallIntegerField(verbose_name='Descrição', choices=DESCRICAO_CHOICES, unique=True)

    class Meta:
        verbose_name = 'Área Responsável'
        verbose_name_plural = 'Áreas Responsáveis'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.get_descricao_display()


class Lotacao(models.Model):
    """
    Lotação do equipamento
    """

    sigla = models.CharField(max_length=16)
    nome = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Lotação'
        verbose_name_plural = 'Lotações'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.sigla


class Equipamento(models.Model):
    """
    Descrição do Equipamento
    """

    descricao = models.TextField(verbose_name='Descrição')
    patrimonio = models.CharField(verbose_name='Patrimônio', max_length=64)
    numero_serie = models.CharField(verbose_name='Número de Série', max_length=64)
    observacao = models.CharField(verbose_name='Observação', max_length=128, blank=True)
    fabricante = models.CharField(verbose_name='Fabricante', max_length=64)
    modelo = models.CharField(max_length=64)
    data_cadastro = models.DateTimeField(default=datetime.now, verbose_name='Data de cadastro')
    lotacao = models.ForeignKey(Lotacao, verbose_name='Lotação', related_name='equipamentos')
    disponibilidade = models.BooleanField(verbose_name='Disponível?', default=True)

    class Meta:
        verbose_name = 'Equipamento'
        verbose_name_plural = 'Equipamentos'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.descricao


class Categoria(models.Model):
    """
    Categoria de equipamento
    """

    DESCRICAO_CHOICES = (
        (1, 'Impressora (Matricial)'),
        (2, 'Impressora (Laser)'),
        (3, 'Impressora (Jato de tinta)'),
        (4, 'Scanner'),
        (5, 'Monitor'),
        (6, 'Data-Show'),
        (7, 'Gabinete PC'),
        (8, 'Gabinete Servidor'),
        (9, 'Notebook'),
        (10, 'Estabilizador'),
        (11, 'Filtro de linha'),
        (12, 'Mouse'),
        (13, 'Teclado'),
        (14, 'Fax'),
        (15, 'Switch'),
        (16, 'Hub'),
        (17, 'Modem'),
        (18, 'Roteador Wi-Fi'),
        (19, 'Roteador cabeado'),
        (20, 'Storage')
    )
    descricao = models.SmallIntegerField(verbose_name='Descrição', choices=DESCRICAO_CHOICES, unique=True)
    equipamentos = models.ManyToManyField(Equipamento, related_name='categorias')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def equipamentos_list(self):
        return ['%s' % el for el in self.equipamentos.filter()]

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.get_descricao_display()


class Usuario(models.Model):
    """
    Define usuário e seu nível de privilégio no sistema
    """

    NIVEL_CHOICES = (
        (1, 'Usuário'),
        (2, 'Operador'),
        (3, 'Administrador')
    )

    nome = models.CharField(verbose_name='Nome', max_length=64)
    sobrenome = models.CharField(verbose_name='Sobrenome', max_length=64)
    login = models.CharField(verbose_name='Login', max_length=32)
    matricula = models.CharField(verbose_name='Matrícula', max_length=64)
    senha = models.CharField(verbose_name='Senha', max_length=255)
    email = models.EmailField(verbose_name='E-mail', max_length=75)
    nivel = models.SmallIntegerField(verbose_name='Nível', choices=NIVEL_CHOICES, default='1')
    data_cadastro = models.DateTimeField(default=datetime.now, verbose_name='Data de cadastro')
    area_responsavel = models.ForeignKey(AreaResponsavel, verbose_name='Área Responsável', null=True, related_name='usuarios')
    lotacao = models.ForeignKey(Lotacao, verbose_name='Lotação', related_name='usuarios')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.nome


class Emprestimo(models.Model):
    """
    Registra um empréstimo, bem como suas particularidades
    """

    justificativa = models.TextField()
    data_emprestimo = models.DateTimeField(default=datetime.now, verbose_name='Saída do equipamento')
    data_devolucao = models.DateTimeField(verbose_name='Retorno do equipamento')
    data_limite = models.DateTimeField(verbose_name='Prazo limite para devolução do equipamento')
    observacao = models.TextField(verbose_name='Observação', blank=True)
    responsavel = models.ForeignKey(Usuario, verbose_name='Responsável', related_name='responsavel_emprestimos')
    solicitante = models.ForeignKey(Usuario, related_name='solicitante_emprestimos')
    equipamento = models.ForeignKey(Equipamento, related_name='emprestimos')

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.equipamento.patrimonio


class SLA(models.Model):
    """
    Nível de acordância definido para implementação de cada tipo de serviço
    """

    descricao = models.CharField(verbose_name='Descrição', max_length=64)
    tempo = models.SmallIntegerField()

    class Meta:
        verbose_name = 'SLA'
        verbose_name_plural = 'SLAs'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s %s' % (self.tempo, self.descricao)


class AssistenciaTecnica(models.Model):
    """
    Cadastro de Assistências Técnicas
    """

    razao_social = models.CharField(verbose_name='Razão Social', max_length=64)
    nome_fantasia = models.CharField(max_length=64)
    cnpj = models.CharField(max_length=18)
    contato = models.CharField(max_length=64)
    responsavel = models.CharField(verbose_name='Responsável', max_length=64)
    email = models.EmailField(verbose_name='E-mail', max_length=75)
    fax = models.CharField(max_length=16)
    site = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'Assistência Técnica'
        verbose_name_plural = 'Assistências Técnicas'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.nome_fantasia


class Endereco(models.Model):
    """
    Endereço, seja ele para Usuários ou Assistências Técnicas
    """

    UF_CHOICES = (
        (1, 'AC'),
        (2, 'AL'),
        (3, 'AP'),
        (4, 'AM'),
        (5, 'BA'),
        (6, 'CE'),
        (7, 'DF'),
        (8, 'ES'),
        (9, 'GO'),
        (10, 'MA'),
        (11, 'MT'),
        (12, 'MS'),
        (13, 'MG'),
        (14, 'PA'),
        (15, 'PB'),
        (16, 'PR'),
        (17, 'PE'),
        (18, 'PI'),
        (19, 'RJ'),
        (20, 'RN'),
        (21, 'RS'),
        (22, 'RO'),
        (23, 'RR'),
        (24, 'SC'),
        (25, 'SP'),
        (26, 'SE'),
        (27, 'TO')
    )

    logradouro = models.CharField(max_length=256)
    cidade = models.CharField(max_length=64)
    uf = models.SmallIntegerField(choices=UF_CHOICES)
    cep = models.CharField(max_length=9)
    assistencia_tecnica = models.ForeignKey(AssistenciaTecnica, verbose_name='Assistência Técnica', related_name='enderecos')

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.logradouro


class Solucao(models.Model):
    """
    Caracterização das Soluções dos Problemas
    """

    descricao = models.TextField(verbose_name='Descrição')

    class Meta:
        verbose_name = 'Solução'
        verbose_name_plural = 'Soluções'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.descricao


class Problema(models.Model):
    """
    Caracterização dos Problemas passíveis de demandar serviços de TI
    """

    descricao = models.TextField(verbose_name='Descrição')
    possivel_causa = models.TextField(verbose_name='Possível causa')
    area_responsavel = models.ForeignKey(AreaResponsavel, verbose_name='Área Responsável', related_name='problemas')
    sla = models.ForeignKey(SLA, related_name='problemas')
    solucoes = models.ManyToManyField(Solucao, verbose_name='Solução', related_name='problemas')

    class Meta:
        verbose_name = 'Problema'
        verbose_name_plural = 'Problemas'

    def solucoes_list(self):
        return ['%s' % sl for sl in self.solucoes.filter()]

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.descricao


class Garantia(models.Model):
    """
    Detalhamento da Garantia de serviço prestado por Assistência Técnica
    """

    descricao = models.CharField(verbose_name='Descrição', max_length=64)
    detalhes = models.TextField()

    class Meta:
        verbose_name = 'Garantia'
        verbose_name_plural = 'Garantias'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.descricao


class Chamado(models.Model):
    """
    Núcleo do Sistema. Caracteriza e registra uma demanda de TI.
    """

    desc_chamado = models.TextField(verbose_name='Descrição do Chamado', blank=True)
    data_abertura = models.DateTimeField(default=datetime.now, verbose_name='Data de Abertura')
    data_encerramento = models.DateTimeField(verbose_name='Data de Encerramento', blank=True, null=True)
    desc_problema = models.TextField(verbose_name='Descrição do Problema', blank=True)
    desc_solucao = models.TextField(verbose_name='Descrição da Solução', blank=True)
    area_responsavel = models.ForeignKey(AreaResponsavel, null=True, related_name='chamados')
    equipamento = models.ForeignKey(Equipamento, null=True, related_name='chamados')
    operadores = models.ManyToManyField(Usuario, related_name='operadores_chamados')
    problemas = models.ManyToManyField(Problema, related_name='problemas_chamados')
    usuario = models.ForeignKey(Usuario, verbose_name='Usuário', related_name='usuario_chamados')

    class Meta:
        verbose_name = 'Chamado'
        verbose_name_plural = 'Chamados'

    def operadores_list(self):
        return ['%s' % ol for ol in self.operadores.filter()]

    def problemas_list(self):
        return ['%s' % pl for pl in self.problemas.filter()]

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.desc_chamado


class Status(models.Model):
    """
    Situação/Andamento de um dado serviço de TI
    """

    DESCRICAO_CHOICES = (
        (1, 'Aberto/Aguardando atendimento'),
        (2, 'Em atendimento'),
        (3, 'Situação sendo diagnosticada'),
        (4, 'Equipamento sendo levado para assistência local'),
        (5, 'Enviado à assistência técnica'),
        (6, 'Enviado à outra assistência técnica'),
        (7, 'Retornou da assistência técnica'),
        (8, 'Equipamento(s)/Software(s) sendo testado(s)'),
        (9, 'Encerrado atendimento')
    )

    descricao = models.SmallIntegerField(verbose_name='Descrição', choices=DESCRICAO_CHOICES)
    data_inicial = models.DateTimeField(default=datetime.now)
    data_final = models.DateTimeField()
    chamado = models.ForeignKey(Chamado, related_name='status')

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s - %s - %s - %s' % (self.get_descricao_display(), self.data_inicial, self.data_final, self.chamado)


class Assentamento(models.Model):
    """
    Observações textuais feitas ao longo da execução de um Chamado
    """

    descricao = models.TextField(verbose_name='Descrição')
    chamado = models.ForeignKey(Chamado, null=True, related_name='assentamentos')

    class Meta:
        verbose_name = 'Assentamento'
        verbose_name_plural = 'Assentamentos'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.descricao


class AtendimentoExterno(models.Model):
    """
    Registro de Serviço de Atendimento de Assistência Técnica, no caso da impossibilidade de se resolver internamente
    """

    descricao = models.TextField(verbose_name='Descrição')
    data_saida = models.DateTimeField(default=datetime.now, verbose_name='Data de Saída')
    data_retorno = models.DateTimeField(verbose_name='Data de Retorno')
    custo = models.FloatField()
    assistencia_tecnica = models.ForeignKey(AssistenciaTecnica, verbose_name='Assistências técnicas', related_name='atendimentos_externos')
    chamado = models.ForeignKey(Chamado, related_name='atendimentos_externos')
    garantia = models.ForeignKey(Garantia, related_name='atendimentos_externos')

    class Meta:
        verbose_name = 'Atendimento Externo'
        verbose_name_plural = 'Atendimentos Externos'

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s' % self.descricao


class Telefone(models.Model):
    """
    Registro de Telefones das Assistências Técnicas
    """

    TIPO_CHOICES = (
        (1, 'Público'),
        (2, 'Residencial'),
        (3, 'Celular')
    )

    OPERADORA_CHOICES = (
        (1, 'Oi'),
        (2, 'Vivo'),
        (3, 'Claro'),
        (4, 'TIM'),
        (5, 'Amazon')
    )

    tipo = models.SmallIntegerField(choices=TIPO_CHOICES, null=True)
    ddi = models.CharField(max_length=4, blank=True, null=True, default='+55')
    ddd = models.CharField(max_length=4, default='63')
    numero = models.CharField(max_length=10)
    operadora = models.SmallIntegerField(choices=OPERADORA_CHOICES, null=True)
    lotacao = models.ForeignKey(Lotacao, related_name='telefones', null=True)
    assistencia_tecnica = models.ForeignKey(AssistenciaTecnica, related_name='telefones', null=True)

    def __str__(self):  # Python 2: def __unicode__(self):
        return '%s - (%s) %s' (self.operadora, self.ddd, self.numero)
