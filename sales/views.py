from django.shortcuts import render, redirect
from .models import Sales



def sales(request):
    sales=Sales.objects
    return render (request, 'sales/sales.html',{'sales':sales})

def salesform(request):
    return render (request, 'sales/sales_form.html')

def postsale(request):
    print(request.method)
    if(request.method)=="POST":
        #print("Sucess!")
        date=request.POST.get("date")
        customer=request.POST.get("customer")
        phonenumber=request.POST.get("phonenumber")
        location=request.POST.get("location")
        email=request.POST.get("email")
        product=request.POST.get("product")
        units=request.POST.get("units")
        unitmeasure=request.POST.get("unitmeasure")
        unitprice=request.POST.get("unitprice")
        salesperson=request.POST.get("salesperson")
        paymentmode=request.POST.get("paymentmode")
        # print(date,customer,phonenumber,email,location,product,units,unitmeasure,unitprice,salesperson,paymentmode)
        salerecord=Sales(date=date,customer=customer,phonenumber=phonenumber,location=location,
                         email=email,product=product,units=units,unitmeasure=unitmeasure,
                         unitprice=unitprice,salesperson=salesperson,paymentmode=paymentmode)
        salerecord.save()
        sales=Sales.objects
    return render (request, 'sales/sales.html',{'sales':sales})
