from django.apps import AppConfig


class AnalisadorConfig(AppConfig):
    name = 'analisador'
    verbose_name = 'Analisador'

    def ready(self):
        import analisador.signals
