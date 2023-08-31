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
    response = 0
    data = 0
    res = 0
    convert_amount = 0
    if request.method == 'POST':
        form = FormCurrency(request.POST)
        if form.is_valid():
            form.save()
            price = form.cleaned_data['amount']
            from_cur = form.cleaned_data['from_currency']
            to_cur = form.cleaned_data['to_currency']







            # client = currencyapicom.Client(KEY)
            # res = client.convert(price, currencies=[from_cur, to_cur])
            # print(res)
            # url = f'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest?amount={price}&from={from_cur}&to={to_cur}'
            # url = f'http://data.fixer.io/api/convert?access_key={KEY}&from={from_cur}&to={to_cur}&amount={price}'
            # url = f"https://api.frankfurter.app/latest?amount={price}&from={from_cur}&to={to_cur}"
            # url = 'http://data.fixer.io/api/convert'
            # url = f'http://api.exchangeratesapi.io/v1/latest?access_key={KEY}/{from_cur}'
            # res = convert(amount=price, to=[from_cur, to_cur])
            # url = f"https://currency-converter5.p.rapidapi.com/currency/convert?amount={price}&code={from_cur}&to={to_cur}"
            # querystring = {"format": "json", from_cur: "AUD", to_cur: "CAD", price: "1"}
            # headers = {
            #     "X-RapidAPI-Key": "79e75d7097mshf9b9f5ed68072f0p1ed4b9jsn4be3db96a611",
            #     "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
            # }
            #
            # response = requests.get(url, headers=headers)

            # url = f'https://api.currencyapi.com/v3/convert?apikey=cur_live_2z6pTccGCoy6R13dzJYqdVW7jpXweq1RRuoH7vSy?&from={from_cur}&to={to_cur}&value={price}'
            # response = requests.get(url)
            # data = response.json()
            # exchange_rate = data['rates'][to_cur]
            # convert_amount = price * exchange_rate
            data = cur.convert().base(from_cur).target(to_cur).amount(price).get()
            data = data[0]['converted_amount']

    else:
        form = FormCurrency()
    return render(request, 'exchange/index.html', {'form': form, 'res': data})




# def res(request):
#     amount = request.POST.get('amount')
#     from_currency = request.POST.get('from_currency')
#     to_currency = request.POST.get('to_currency')
#     url = f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}"
#     response = requests.get(url)
#     return render(request, 'exchange/result.html', {'res': response})
