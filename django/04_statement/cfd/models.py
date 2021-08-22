from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.
class Statement(models.Model):
    ticket = models.IntegerField()
    open_time = models.CharField(max_length=255)
    type_st = models.CharField(max_length=255)
    size_st = models.FloatField()
    item_st = models.CharField(max_length=255)
    open_price = models.FloatField()
    s_l = models.FloatField(null=True, blank=True)
    t_p = models.FloatField(null=True, blank=True)
    close_time = models.CharField(max_length=255)
    close_price = models.FloatField()
    commission = models.FloatField()
    taxes = models.IntegerField(null=True, blank=True)
    swap = models.IntegerField(null=True, blank=True)
    profit = models.FloatField(null=True, blank=True)

    objects = DataFrameManager()
    # def __str__(self):
    #     return self.open_time
