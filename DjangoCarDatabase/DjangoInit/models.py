
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime

# Create your models here.
class Part(models.Model):
    number = models.IntegerField(default=0)
    name = models.CharField(max_length=512)
    description = models.TextField()

class Customer(models.Model):
    first_name = models.CharField(max_length=512)

class carMake(models.Model):
    manufacturer = models.CharField(max_length=512)

class Car(models.Model):
    model = models.CharField(max_length=512)
    year = models.IntegerField(default=0)
    manufacturer = models.ForeignKey(carMake)

class purchasedBy(models.Model):
    date = models.DateTimeField(auto_now_add=True,blank=True)
    customer = models.ForeignKey(Customer)
    part = models.ForeignKey(Part)

class fitsCar(models.Model):
    part = models.ForeignKey(Part)
    car = models.ForeignKey(Car, related_name='parts_that_fit')
    #make = models.ForeignKey(carMake)
