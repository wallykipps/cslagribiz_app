from django import forms
from .models import Sales

class DataForm(forms.ModelForm):
    class Meta:
        model= Sales
        fields= ["date", "customer", "phonenumber", "location","product","salesperson","paymentmode","unitmeasure","units","unitprice"]
