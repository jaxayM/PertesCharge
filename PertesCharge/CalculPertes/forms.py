from django import forms

class Input(forms.Form):
    diametre = forms.FloatField()
    longeur = forms.FloatField()
    rugosite = forms.FloatField()
    debit = forms.FloatField()
    viscosite = forms.FloatField()
    massevol = forms.FloatField()
