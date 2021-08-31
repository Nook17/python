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
    tp_buy = models.IntegerField(null=True, blank=True)
    tp_sell = models.IntegerField(null=True, blank=True)

    objects = DataFrameManager()


class Buy_calc(models.Model):
    buy_level = models.IntegerField()

    objects = DataFrameManager()


class Sell_calc(models.Model):
    sell_level = models.IntegerField()

    objects = DataFrameManager()
