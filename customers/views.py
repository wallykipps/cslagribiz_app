from django.shortcuts import render
from.models import Customers

def customers(request):
    return render(request,'customers/customers.html')
