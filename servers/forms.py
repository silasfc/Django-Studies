# -*- coding: utf-8 -*-

from django import forms
from servers.models import Server


class ServerForm(forms.ModelForm):

    class Meta:
        model = Server
        fields = ['name', 'ip', 'order']
