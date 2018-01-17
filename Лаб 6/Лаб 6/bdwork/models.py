# -*- coding: utf-8 -*-
from django.db import models


class My_user(models.Model):
    class Meta:
        db_table = "Users"
    first_name = models.CharField(max_length = 50)
    second_name = models.CharField(max_length=50)
    group = models.CharField(max_length= 15)
    birthday = models.DateField()



class Ser_f_users(models.Model):
    class Meta():
        db_table = "Serveses"
    price = models.IntegerField(verbose_name="цена")
    type_of_serves = models.CharField(max_length=50, verbose_name='тип услуги')
    customer = models.ForeignKey(My_user)
    use_of_serves = models.IntegerField(default=0)