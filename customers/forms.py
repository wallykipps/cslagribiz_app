from django import forms
#from django.db.models import CharField, Value as V
#from django.db.models.functions import Concat
from .models import Customers

class customerForm(forms.ModelForm):
    class Meta:
        model = Customers
        #fields = "__all__"
        fields = ['reg_date','firstname','lastname','phonenumber', 'email','location']
        widgets = {#'reg_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        'reg_date': forms.DateInput(attrs={'class': 'form-control text-input','type': 'date','required': True}, format='%Y-%m-%d'),
        'firstname': forms.TextInput(attrs={ 'class': 'form-control' , 'placeholder':'First Name', 'required': True}),
        'lastname': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder':'Last Name', 'required': True }),
        'phonenumber': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder':'Phone Number', 'required': True }),
        'email': forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder':'Email','required': False }),
        'location': forms.TextInput(attrs={ 'class': 'form-control' , 'placeholder':'Location', 'required': True }),
        #'customername': forms.TextInput(attrs={'class': 'form-control' , 'placeholder':'Customer Name', 'required': True}),
        }
