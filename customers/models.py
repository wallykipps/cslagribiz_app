from django.db import models

class Customers(models.Model):
    date=models.DateField()
    customer=models.CharField(max_length=255,)
    phonenumber=models.CharField(max_length=255)
    email=models.EmailField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True, null=True)

def __str__(self):
    return self.customer
