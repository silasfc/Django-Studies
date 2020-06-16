from django.db import models
from analisador.const import MMA_INTERVAL, MME_INTERVAL, k_value_on_mme, N_MAIORES_BM, ABREVIATURA_ACOES_CHOICES, NOME_ACOES_CHOICES, DECISAO_CHOICES


class Acao(models.Model):
    abreviatura = models.PositiveSmallIntegerField(verbose_name='Abreviatura', choices=ABREVIATURA_ACOES_CHOICES)
    nome_fantasia = models.PositiveSmallIntegerField(verbose_name='Nome Fantasia', choices=NOME_ACOES_CHOICES)

    class Meta:
        ordering = ('abreviatura',)
        verbose_name = 'Ação'
        verbose_name_plural = 'Ações'

    def __str__(self):  # __unicode__ on Python 2
        return self.get_nome_fantasia_display()


class Dado(models.Model):
    '''
    Modelo das médias e demais dados
    '''
    acao = models.ForeignKey('Acao', verbose_name='Nome', related_name='dados')
    data = models.DateField(verbose_name='Data')
    valor_fechamento = models.FloatField(verbose_name='Valor de Fechamento', null=True)  # Fechamento|ajust p/ prov|em moeda orig
    vpa = models.FloatField(verbose_name='Valor Patrimonial da Ação', null=True)  # VPA|em moeda orig|consolid:sim*|ajust p/ prov
    vpa_p_bm = models.FloatField(verbose_name='B2M', null=True, blank=True)  # vpa / valor_fechamento
    mma = models.FloatField(verbose_name='MMA' + str(MMA_INTERVAL), null=True, blank=True)  # média dos últimos 40 valor_fechamento
    mme = models.FloatField(verbose_name='MME' + str(MME_INTERVAL), null=True, blank=True)  # ( (valor_fechamento do dia - mme do dia útil anterior) * k_value_on_mme) + mme do dia útil anterior
    dif_mme_mma = models.FloatField(verbose_name='MME - MMA', null=True, blank=True)  # (MME - MMA)
    correlacao = models.FloatField(verbose_name='Correlação', null=True, blank=True)  # ???

    class Meta:
        ordering = ('data', 'acao__nome_fantasia')
        unique_together = ('acao', 'data')
        verbose_name = 'Dado'
        verbose_name_plural = 'Dados'

    def __str__(self):  # __unicode__ on Python 2
        return str(self.acao) + ' - ' + self.data.strftime('%d/%m/%Y')

    def save(self, *args, **kwargs):
        self.vpa_p_bm = self.get_vpa_p_bm
        self.mma = self.get_mma
        self.mme = self.get_mme
        self.dif_mme_mma = (self.mme - self.mma) if (self.mme and self.mma) else None
        super().save(*args, **kwargs)

    @property
    def get_vpa_p_bm(self):
        if not hasattr(self, '_vpa_p_bm'):
            self._vpa_p_bm = self.vpa / self.valor_fechamento if (self.valor_fechamento and self.vpa) else None

        return self._vpa_p_bm

    @property
    def get_mma(self):
        if not hasattr(self, '_mma'):
            mma_anteriores = Dado.objects.filter(acao=self.acao, data__lte=self.data)

            if mma_anteriores.count() >= MMA_INTERVAL:
                media_vf = mma_anteriores.order_by('-data')[:MMA_INTERVAL].aggregate(models.Avg('valor_fechamento'))
                self._mma = media_vf.get('valor_fechamento__avg')
            else:
                self._mma = None

        return self._mma

    @property
    def get_mme(self):
        if not hasattr(self, '_mme'):
            mme_anteriores = Dado.objects.filter(acao=self.acao, data__lte=self.data)

            if mme_anteriores.count() < MME_INTERVAL:
                self._mme = None
            elif mme_anteriores.count() == MME_INTERVAL:
                media_vf = mme_anteriores.order_by('-data')[:MME_INTERVAL].aggregate(models.Avg('valor_fechamento'))
                self._mme = media_vf.get('valor_fechamento__avg')
            else:
                consulta = mme_anteriores.filter(data__lt=self.data).order_by('data')
                previous_mme = consulta.last().mme if consulta.exists() else 0
                self._mme = (self.valor_fechamento - previous_mme) * k_value_on_mme + previous_mme

        return self._mme

    @classmethod
    def get_n_maiores_bm(cls, data=None, n=N_MAIORES_BM):
        return cls.objects.filter(data=data).order_by('-vpa_p_bm')[:n]

    @classmethod
    def list_datas(cls):
        datas = cls.objects.distinct('data').values_list('data', flat=True)
        return datas

    @property
    def get_decisao(self):
        pass


class Analise(models.Model):
    dado = models.ForeignKey(Dado, verbose_name='Dado', related_name='analises')
    data = models.DateField(verbose_name='Data de referência')
    ordem = models.PositiveSmallIntegerField(verbose_name='Ordem')
    decisao = models.PositiveSmallIntegerField(verbose_name='Decisão', choices=DECISAO_CHOICES, default=3)

    class Meta:
        ordering = ('data', 'ordem')
        unique_together = ('data', 'ordem')
        verbose_name = 'Análise'
        verbose_name_plural = 'Análises'

    def __str__(self):
        return str(self.ordem) + 'º - ' +\
            self.data.strftime('%d/%m/%Y') + ': ' +\
            str(self.dado.acao.get_nome_fantasia_display())

    @property
    def ordinal(self):
        return str(self.ordem) + 'º'
