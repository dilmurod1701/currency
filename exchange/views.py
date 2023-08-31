from django.shortcuts import render

from .forms import FormCurrency

import requests
import currencyapicom
from py_currency_converter import convert
from currency_converter_with_rate import currency

cur = currency.Currency()


# Create your views here.
KEY = '13a0b1c6d3c8271e6ae8a881e0ce49a6'


def convert_currency(request):
    data = 0
    if request.method == 'POST':
        form = FormCurrency(request.POST)
        if form.is_valid():
            form.save()
            price = form.cleaned_data['amount']
            from_cur = form.cleaned_data['from_currency']
            to_cur = form.cleaned_data['to_currency']
            data = cur.convert().base(from_cur).target(to_cur).amount(price).get()
            data = data[0]['converted_amount']

    else:
        form = FormCurrency()
    return render(request, 'exchange/index.html', {'form': form, 'res': data})



