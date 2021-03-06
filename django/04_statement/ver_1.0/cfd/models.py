from django.db import models
from django_pandas.managers import DataFrameManager


# Create your models here.
class Statement(models.Model):
    ticket = models.IntegerField()
    open_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    type_st = models.CharField(max_length=255)
    size_st = models.FloatField()
    item_st = models.CharField(max_length=255)
    open_price = models.FloatField()
    s_l = models.FloatField(null=True, blank=True)
    t_p = models.FloatField(null=True, blank=True)
    close_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    close_price = models.FloatField()
    commission = models.FloatField()
    taxes = models.FloatField(null=True, blank=True)
    swap = models.FloatField(null=True, blank=True)
    profit = models.FloatField(null=True, blank=True)

    objects = DataFrameManager()
    # def __str__(self):
    #     return self.open_time


class Deposit(models.Model):
    date_dep = models.DateTimeField(auto_now=False, auto_now_add=False)
    amount_dep = models.FloatField()
    bank_name = models.CharField(max_length=255)

    objects = DataFrameManager()


class Withdrawal(models.Model):
    date_wd = models.DateTimeField(auto_now=False, auto_now_add=False)
    amount_wd = models.FloatField()
    bank_name = models.CharField(max_length=255)

    objects = DataFrameManager()


class Notesdb(models.Model):
    percent_year = models.FloatField(null=True, blank=True)
    amount_year = models.IntegerField(null=True, blank=True)
    forex_start = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    margin_value = models.IntegerField(null=True, blank=True)
    pip_value = models.FloatField(null=True, blank=True)
    gap = models.IntegerField(null=True, blank=True)
    lot = models.FloatField(null=True, blank=True)
    tp = models.IntegerField(null=True, blank=True)
    buy_or_sell = models.CharField(max_length=255, null=True, blank=True)
    amount_quarter = models.IntegerField(null=True, blank=True)
    percent_1 = models.FloatField(null=True, blank=True)
    percent_2 = models.FloatField(null=True, blank=True)
    percent_3 = models.FloatField(null=True, blank=True)
    daily_point = models.IntegerField(null=True, blank=True)
    lot_value = models.FloatField(null=True, blank=True)

    objects = DataFrameManager()


class Buy_calc(models.Model):
    buy_level = models.IntegerField()

    objects = DataFrameManager()


class Quarter(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    profit = models.IntegerField(null=True, blank=True)

    objects = DataFrameManager()


class Pipmargin(models.Model):
    market = models.CharField(max_length=255)
    margin = models.IntegerField()
    pip = models.FloatField()
    updated_at = models.DateTimeField(auto_now=True)

    objects = DataFrameManager()



'''
Quarter
-------
id
date - DateTimeField
profit - FloatField


Notesdb
-------
amount_quarter - IntegerField
percent_1 - FloatField
percent_2 - FloatField
percent_3 - FloatField

'''
