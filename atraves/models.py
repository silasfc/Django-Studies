from django.db import models
from datetime import datetime, date


BOOLEAN_CHOICES = (
    (1, 'Não informado'),
    (2, 'Sim'),
    (3, 'Não')
)

class NaturalPerson(models.Model):
    name = models.TextField(verbose_name='Nome')

    class Meta:
        verbose_name = 'Pessoa Física'

    def __str__(self):
        return '%s' % self.name


class Involved(models.Model):
    person = models.ForeignKey(NaturalPerson, verbose_name='Envolvido')
    incident = models.ForeignKey('Incident', verbose_name='Caso', null=True)

    class Meta:
        verbose_name = 'Envolvido'
        abstract = True

    def __str__(self):
        return '%s' % self.person


class Victim(Involved):
    '''
    Classe que caracteriza a ação da Vítima em um dado caso.
    '''

    BEHAVIOR_PROCESS_CHOICES = (
        (1, 'Não localizada'),
        (2, 'Intimada, não comparece'),
        (3, 'Confirmou agressão - está reconciliada'),
        (4, 'Confirmou agressão - não está reconciliada'),
        (5, 'Negou agressão - não está reconciliada'),
        (6, 'Negou agressão - está reconciliada')
    )

    RELIGIOUS_UNDERSTANDING_CHOICES = (
        (1, 'Não informado'),
        (2, 'Ate'),
        (3, 'Candomblé'),
        (4, 'Espírita'),
        (5, 'Muçulmano'),
        (6, 'Protestante'),
        (7, 'Agnóstico'),
        (8, 'Budista'),
        (9, 'Católico'),
        (10, 'Judaico'),
        (11, 'Pentecostal'),
        (12, 'Nenhum')
    )

    interview_date = models.DateTimeField(verbose_name='Data da entrevista', auto_now_add=True)
    behavior_process = models.IntegerField(choices=BEHAVIOR_PROCESS_CHOICES, verbose_name='Comportamento da vítima no processo')
    wish_proceed = models.IntegerField(choices=BOOLEAN_CHOICES, verbose_name='Deseja prosseguir com o processo?', null=True)
    religious_understanding = models.IntegerField(choices=RELIGIOUS_UNDERSTANDING_CHOICES, verbose_name='Entendimento religioso', null=True)
    observation = models.TextField(verbose_name='Observação', blank=True)

    def wish_proceed_reply(self):
        return 'Sim' if self.wish_proceed else 'Não'

    class Meta:
        verbose_name = 'Vítima'


class Offender(Involved):
    '''
    Classe que caracteriza a ação do Agressor em um dado caso.
    '''

    BEHAVIOR_PROCESS_CHOICES = (
        (1, 'Confessou'),
        (2, 'Nego')
    )

    PROFESSIONAL_GUIDANCE_CHOICES = (
        (1, 'Não'),
        (2, 'Sim'),
        (3, 'Já faz tratamento')
    )

    behavior_process = models.IntegerField(verbose_name='Comportamento do agressor no processo', choices=BEHAVIOR_PROCESS_CHOICES)
    professional_guidance = models.IntegerField(verbose_name='Orientação profissional', choices=PROFESSIONAL_GUIDANCE_CHOICES)

    class Meta:
        verbose_name = 'Agressor'


class Incident(models.Model):
    '''
    Classe que define o caso, onde participam Agressor e Vítima.
    '''

    FINAL_RESULT_CHOICES = (
        (1, 'Condenação'),
        (2, 'Absolvição')
    )

    number = models.SmallIntegerField(null=True)
    year = models.SmallIntegerField(null=True)
    cache_number = models.CharField(max_length=10, null=True, db_index=True)
    date_time = models.DateTimeField(verbose_name='Data e hora')
    final_result = models.IntegerField(verbose_name='Resultado Final', choices=FINAL_RESULT_CHOICES, null=True)
    observation = models.TextField(verbose_name='Observação', blank=True)
    offenders = models.ManyToManyField(NaturalPerson, verbose_name='Agressor(es)', related_name='incidents_offenders', through=Offender)
    victims = models.ManyToManyField(NaturalPerson, verbose_name='Vítima(s)', related_name='incidents_victims', through=Victim)

    def offenders_list(self):
        return ['%s' % ol for ol in self.offenders.filter()]

    def victims_list(self):
        return ['%s' % vl for vl in self.victims.filter()]

    def next_number(self):
        query = self.__class__.objects.filter(
            year=self.year
        ).order_by(
            'number'
        ).aggregate(
            max_number=models.Max('number')
        )

        return int(query.get('max_number') or 0) + 1

    def save(self, *args, **kwargs):
        if not self.number:
            self.year = self.year if self.year else date.today().year
            self.number = self.next_number()

        self.cache_number = '%03d/%d' % (
            self.number,
            self.year
        )

        super(Incident, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Caso'

    def __str__(self):
        return '%s' % (self.cache_number)
