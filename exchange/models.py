from django.db import models


# Create your models here.


class Currency(models.Model):
    CHOICE = (
        ('AFN', 'AFN'),
        ('ALL', 'ALL'),
        ('DZD', 'DZD'),
        ('ARS', 'ARS'),
        ('AMD', 'AMD'),
        ('AUD', 'AUD'),
        ('AZN', 'AZN'),
        ('BSD', 'BSD'),
        ('BHD', 'BHD'),
        ('BDT', 'BDT'),
        ('BBD', 'BBD'),
        ('BYN', 'BYN'),
        ('EUR', 'EUR'),
        ('BZD', 'BZD'),
        ('XOF', 'XOF'),
        ('BTN', 'BTN'),
        ('BOB', 'BOB'),
        ('BAM', 'BAM'),
        ('BWP', 'BWP'),
        ('BRL', 'BRL'),
        ('BND', 'BND'),
        ('BGN', 'BGN'),
        ('CAD', 'CAD'),
        ('XAF', 'XAF'),
        ('CNY', 'CNY'),
        ('COP', 'COP'),
        ('CRC', 'CRC'),
        ('CUP', 'CUP'),
        ('CZK', 'CZK'),
        ('CDF', 'CDF'),
        ('DKK', 'DKK'),
        ('USD', 'USD'),
        ('EGP', 'EGP'),
        ('HUF', 'HUF'),
        ('ISK', 'ISK'),
        ('INR', 'INR'),
        ('IDR', 'IDR'),
        ('IRR', 'IRR'),
        ('IQD', 'IQD'),
        ('ILS', 'ILS'),
        ('JPY', 'JPY'),
        ('KZT', 'KZT'),
        ('KPW', 'KPW'),
        ('KRW', 'KRW'),
        ('KGS', 'KGS'),
        ('LAK', 'LAK'),
        ('LRD', 'LRD'),
        ('MGA', 'MGA'),
        ('MYR', 'MYR'),
        ('MXN', 'MXN'),
        ('MAD', 'MAD'),
        ('NZD', 'NZD'),
        ('NGN', 'NGN'),
        ('NOK', 'NOK'),
        ('PKR', 'PKR'),
        ('ILS', 'ILS'),
        ('PYG', 'PYG'),
        ('PLN', 'PLN'),
        ('QAR', 'QAR'),
        ('RUB', 'RUB'),
        ('SAR', 'SAR'),
        ('XOF', 'XOF'),
        ('SEK', 'SEK'),
        ('CHF', 'CHF'),
        ('TJS', 'TJS'),
        ('THB', 'THB'),
        ('TRY', 'TRY'),
        ('TMT', 'TMT'),
        ('UAH', 'UAH'),
        ('AED', 'AED'),
        ('GBP', 'GBP'),
        ('UYU', 'UYU'),
        ('UZS', 'UZS'),
        ('VEF', 'VEF'),
        ('YER', 'YER'),
    )
    from_currency = models.CharField(max_length=100, choices=CHOICE, db_column='from')
    to_currency = models.CharField(max_length=100, choices=CHOICE, db_column='to')
    amount = models.BigIntegerField()

    def __str__(self):
        return f"{self.from_currency} to {self.to_currency}"

    class Meta:
        db_table = 'currency'
