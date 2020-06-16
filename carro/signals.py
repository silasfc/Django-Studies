from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from .models import Peca, Servico


@receiver(post_delete, sender=Peca)
@receiver(post_save, sender=Peca)
def update_custo_peca_on_revisao(sender, instance, **kwargs):
    instance.revisao.save()


@receiver(post_delete, sender=Servico)
@receiver(post_save, sender=Servico)
def update_custo_servico_on_revisao(sender, instance, **kwargs):
    instance.revisao.save()
