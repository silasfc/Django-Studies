# -*- coding: utf-8 -*-

from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(max_length=60)

    def __str__(self):  # Python 3: def __str__(self):
        return self.nome


class Telefone(models.Model):
    TIPOS_DE_TELEFONES = (
        ('R', 'Residencial'),  # Exibe 'Residencial', mas persiste 'R' no banco
        ('C', 'Celular'),
    )

    numero = models.CharField(max_length=15)
    tipo = models.CharField(max_length=11, choices=TIPOS_DE_TELEFONES, default='R')

    def __str__(self):  # Python 3: def __str__(self):
        return self.numero


class Email(models.Model):
    TIPOS_DE_EMAILS = (
        ('P', 'Pessoal'),  # Exibe 'Pessoal', mas persiste 'P' no banco
        ('I', 'Institucional'),
    )

    endereco = models.CharField(max_length=35)
    tipo = models.CharField(max_length=13, choices=TIPOS_DE_EMAILS, default='P')

    def __str__(self):  # Python 3: def __str__(self):
        return self.endereco


class Cadastro(models.Model):
    nome = models.ForeignKey(Pessoa, related_name='+')
    pai = models.ForeignKey(Pessoa, related_name='+')
    mae = models.ForeignKey(Pessoa, related_name='+')
    data_nascimento = models.DateField(null=True)  # ...ou DateTimeField
    endereco = models.CharField(max_length=50, null=True)
    email_pessoal = models.ForeignKey(Email, related_name='+')
    email_institucional = models.ForeignKey(Email, related_name='+', null=True)
    telefone_residencial = models.ForeignKey(Telefone, related_name='+', null=True)
    telefone_celular = models.ForeignKey(Telefone, related_name='+')

    def __str__(self):  # Python 3: def __str__(self):
        return u'%s' % self.nome
