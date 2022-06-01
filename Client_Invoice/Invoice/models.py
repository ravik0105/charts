from datetime import datetime
from itertools import chain
from multiprocessing.connection import Client
from operator import mod
from pickle import TRUE
from random import choices
from turtle import position
from typing import Type
from django.db import models
from django.forms import CharField, DateField

# Create your models here.
class Current_Year(models.Model):
    status_sal=(
        ('PAID','PAID'),
        ('Invoiced','Invoiced'),
        ('Offered','Offered'),
        ('Joined','Joined'),
        ('Offer Declined','Offer Declined'),
    )
    s_no=models.AutoField(primary_key=True,auto_created=True)
    Name=models.CharField(max_length=100)
    Clint=models.CharField(max_length=100)
    Position=models.CharField(max_length=100,blank=True, null=True)
    Empsalary=models.IntegerField(blank=True, null=True)
    Billing=models.IntegerField(blank=True, null=True)

    status_type=(
        ('PERMANENT','PERMANENT'),
        ('CONTRACT','CONTRACT')
    )
    Type=models.CharField(max_length=50, choices=status_type)
    Status=models.CharField(max_length=50, choices=status_sal)
    Invoice=models.CharField(max_length=100,blank=True, null=True)
    Doj=models.DateField(blank=True, null=True)
    Invoiced_on=models.DateField(blank=True, null=True)
    Payment_on=models.DateField(blank=True, null=True)
    Total=models.IntegerField(blank=True, null=True)
    status_month=(

        ('01 - Jan','01 - Jan'),
        ('02 - Feb','02 - Feb'),
        ('03 - Mar','03 - Mar'),
        ('04 - Apr','04 - Apr'),
        ('05 - May','05 - May'),
        ('06 - Jun','06 - Jun'),
        ('07 - Jul','07 - Jul'),
        ('08 - Aug','08 - Aug'),
        ('09 - Sep','09 - Sep'),
        ('10 - Oct','10 - Oct'),
        ('11 - Nov','11 - Nov'),
        ('12 - Dec','12 - Dec'),

    )

    Collection=models.CharField(max_length=100,blank=True, null=True)

    Recruiter=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return f'{self.Name}'




class Backup_Year(models.Model):
    status_sal=(
        ('PAID','PAID'),
        ('Invoiced','Invoiced'),
        ('Offered','Offered'),
        ('Joined','Joined'),
        ('Offer Declined','Offer Declined'),
    )
    s_no=models.AutoField(primary_key=True,auto_created=True)
    Name=models.CharField(max_length=100)
    Clint=models.CharField(max_length=100)
    Position=models.CharField(max_length=100, blank=True, null=True)
    Empsalary=models.IntegerField(blank=True, null=True)
    Billing=models.IntegerField(blank=True, null=True)

    status_type=(
        ('PERMANENT','PERMANENT'),
        ('CONTRACT','CONTRACT')
    )
    Type=models.CharField(max_length=50, choices=status_type)
    Status=models.CharField(max_length=50, choices=status_sal)
    Invoice=models.CharField(max_length=100,blank=True, null=True)
    Doj=models.DateField(blank=True, null=True)
    Invoiced_on=models.DateField(blank=True, null=True)
    Payment_on=models.DateField(blank=True, null=True)
    Total=models.IntegerField(blank=True, null=True)
    status_month=(

        ('01 - Jan','01 - Jan'),
        ('02 - Feb','02 - Feb'),
        ('03 - Mar','03 - Mar'),
        ('04 - Apr','04 - Apr'),
        ('05 - May','05 - May'),
        ('06 - Jun','06 - Jun'),
        ('07 - Jul','07 - Jul'),
        ('08 - Aug','08 - Aug'),
        ('09 - Sep','09 - Sep'),
        ('10 - Oct','10 - Oct'),
        ('11 - Nov','11 - Nov'),
        ('12 - Dec','12 - Dec'),

    )

    Collection=models.CharField(max_length=100,blank=True, null=True)

    Recruiter=models.CharField(max_length=50,null=False,blank=False)

    def __str__(self):
        return f'{self.Name}'
