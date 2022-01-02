from enum import auto
from django.db import models
from django.db.models.fields import CharField
from django.contrib.auth.models import User


# Create your models here.


# Abstract Class for Users information 
class Person_info(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    class Meta:
        abstract = True
        ordering = ['name']


# Class when User files Work Order Complaint and will go to the database where Staff and Admin and view and send orders
class reportData(Person_info):
    priority = [
    ('PL','Plumbing'),
    ('EL', 'Electrical'),
    ('MT','Maintenance'),
    ('CAS','CUSTODIAL'),
    ('ENG', 'Engineering'),
    ('EXT', 'Exterminator' )
    ]

    floor = models.IntegerField()
    apt_num = models.CharField(max_length=200)
    complant = models.TextField()
    cateogry = models.CharField(max_length=50, choices=priority)

    class Meta:
        verbose_name_plural = 'Work Orders'


    def __str__(self):
        return f'{self.name}-{self.cateogry}'
    



#Possible idea -> This class was meant for to keep track of which staff sent out which order. 
# Couldn't execute during period of time bc still learning how signals work in django
class orders_done(models.Model):
    order = models.ForeignKey(reportData, on_delete=models.CASCADE)
    staff = models.ForeignKey(User, models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order} completed from {self.staff.username}'



