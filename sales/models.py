from django.db import models

class Sales(models.Model):
    date=models.DateField()
    customer=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=255)
    email=models.EmailField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True, null=True)
    product=models.CharField(max_length=255)
    salesperson=models.CharField(max_length=255)
    paymentmode=models.CharField(max_length=255)
    unitmeasure=models.CharField(max_length=255)
    units=models.IntegerField()
    unitprice=models.DecimalField(max_digits=5, decimal_places=2)

    def total(self):
        total= self.units*self.unitprice
        return total

    def date1(self):
        return self.date.strftime('%e %b %y')

    def __str__(self):
        return self.customer
