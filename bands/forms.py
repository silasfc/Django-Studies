from django import forms
from .models import Band, Member


class BandContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class BandForm(forms.ModelForm):

    class Meta:
        model = Band
        fields = ('name', 'can_rock')


class MemberForm(forms.ModelForm):

    class Meta:
        model = Member
        fields = ('name', 'instrument')
