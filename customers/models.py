from django.db import models
from django.core.validators import RegexValidator
from django.db.models import CharField, Value
from django.db.models.functions import Concat

class Customers(models.Model):
    reg_date=models.DateField()
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=10)
    email=models.EmailField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True)

    def reg_date_2(self):
        return self.reg_date.strftime('%d %b %y')

    def reg_date_1(self):
        return self.reg_date.strftime('%F')

    def customername(self):
        return self.firstname + " " + self.lastname

    class Meta:
        db_table="customers_customers"
        ordering=["-reg_date"]
