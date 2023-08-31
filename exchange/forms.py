from django import forms

from .models import Currency


class FormCurrency(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ['amount', 'from_currency', 'to_currency']
