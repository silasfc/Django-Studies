from django.db import models
from django.utils.translation import gettext as _


class Person(models.Model):
    name = models.CharField(max_length=60, verbose_name=_('Name'))

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self):
        return self.name


class Telephone(models.Model):
    KIND_OF_TELEPHONES = (
        (1, _('Phone')),  # Show 'Phone', but persists 1 on db
        (2, _('Cell Phone'))
    )

    number = models.CharField(max_length=15, verbose_name=_('Number'))
    kind = models.PositiveSmallIntegerField(choices=KIND_OF_TELEPHONES, default=1, verbose_name=_('Kind'))

    class Meta:
        verbose_name = _('Telephone')
        verbose_name_plural = _('Telephones')

    def __str__(self):
        return self.number


class Email(models.Model):
    KIND_OF_EMAIL = (
        (1, _('Personal')),  # Show 'Personal', but persists 1 on db
        (2, _('Institutional')),
    )

    address = models.CharField(max_length=35, verbose_name=_('Address'))
    kind = models.PositiveSmallIntegerField(choices=KIND_OF_EMAIL, default=1, verbose_name=_('Kind'))

    class Meta:
        verbose_name = _('Email')
        verbose_name_plural = _('Emails')

    def __str__(self):
        return self.address


class Register(models.Model):
    name = models.ForeignKey(Person, related_name='+', on_delete=models.PROTECT, verbose_name=_('Name'))
    father = models.ForeignKey(Person, related_name='+', on_delete=models.PROTECT, verbose_name=_('Father'))
    mother = models.ForeignKey(Person, related_name='+', on_delete=models.PROTECT, verbose_name=_('Mother'))
    birth_date = models.DateField(null=True, verbose_name=_('Birth Date'))  # ...or DateTimeField
    address = models.CharField(max_length=50, null=True, verbose_name=_('Address'))
    personal_email = models.ForeignKey(Email, related_name='+', on_delete=models.PROTECT, verbose_name=_('Personal Email'))
    institutional_email = models.ForeignKey(Email, related_name='+', null=True, on_delete=models.PROTECT, verbose_name=_('Institutional Email'))
    phone = models.ForeignKey(Telephone, related_name='+', null=True, on_delete=models.PROTECT, verbose_name=_('Phone'))
    cell_phone = models.ForeignKey(Telephone, related_name='+', on_delete=models.PROTECT, verbose_name=_('Cell Phone'))

    class Meta:
        verbose_name = _('Register')
        verbose_name_plural = _('Registers')

    def __str__(self):
        return u'%s' % self.name
