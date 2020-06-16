from django.db import models


class Contato(models.Model):
    nome = models.CharField(u'Nome', max_length=30)
    sobrenome = models.CharField(u'Sobrenome', max_length=30)
    email = models.EmailField(u'Email', max_length=75)
    twitter = models.URLField(u'Twitter', max_length=200)

    def __str__(self):
        return '%s %s' % (self.nome, self.sobrenome)
