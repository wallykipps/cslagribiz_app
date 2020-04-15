from django.shortcuts import render

def home(request):
    return render(request,'sales/home.html')

def sales(request):
    return render (request, 'sales/sales.html')
