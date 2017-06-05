# -*- coding: utf-8 -*-
# from contrib.utils import getLogger
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from analisador.models import Dado, Analise
import logging

logger = logging.getLogger(__name__)


@receiver(post_delete, sender=Dado)
@receiver(post_save, sender=Dado)
def update_dado(sender, instance, **kwargs):
    for e, d in enumerate(Dado.get_n_maiores_bm(instance.data)):
        Analise.objects.filter(data=instance.data, ordem=e+1).update(dado=d)
        logger.info(d.__str__() + '%s' % u' atualizado...')
