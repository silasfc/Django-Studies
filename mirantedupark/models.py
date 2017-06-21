from django.db import models


class Person(models.Model):
    """Pessoa.

    Classe genérica aproveitada por outras

    """

    class Meta:
        pass

    def __str__():
        pass


class NaturalPerson(Person):
    """Pessoa Física.

    """

    class Meta:
        pass

    def __str__():
        pass


class LegalPerson(Person):
    """Pessoa Jurídica.

    """

    class Meta:
        pass

    def __str__():
        pass


class Owner(models.Model):
    """Condômino.

    """

    class Meta:
        pass

    def __str__():
        pass


class Tenant(models.Model):
    """Inquilino.

    """

    pass

    class Meta:
        pass

    def __str__():
        pass
