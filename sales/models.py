from django.db import models

class Sales(models.Model):
    date=models.DateTimeField()
    customer=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    salesperson=models.CharField(max_length=255)
    paymentmode=models.CharField(max_length=255)
    unitmeasure=models.CharField(max_length=255)
    units=models.DecimalField(max_digits=5, decimal_places=2)
    unitprice=models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.date
