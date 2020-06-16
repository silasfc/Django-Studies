from django.apps import AppConfig


class CarroConfig(AppConfig):
    name = 'carro'
    verbose_name = 'Carro'

    def ready(self):
        from .signals import update_custo_peca_on_revisao
        from .signals import update_custo_servico_on_revisao
