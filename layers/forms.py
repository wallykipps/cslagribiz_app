from django import forms
#from django.forms import ModelForm
#from django.db.models import CharField, Value as V
#from django.db.models.functions import Concat
from .models import LayersCustomers
from .models import LayersSales
from .models import LayersExpenses
from .models import LayersProducts
from .models import LayersProduction
from .models import LayersStockMovement
from .models import LayersEggsInventory
from .models import LayersCashDeposit


class CustomerForm(forms.ModelForm):
    class Meta:
        model = LayersCustomers
        #fields = "__all__"
        fields = ['reg_date','firstname','lastname','phonenumber', 'email','location']
        widgets = {
        'reg_date': forms.DateInput(attrs={'class': 'form-control text-input','type': 'date','required': True}, format='%Y-%m-%d'),
        'firstname': forms.TextInput(attrs={ 'class': 'form-control' , 'placeholder':'First Name', 'required': True}),
        'lastname': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder':'Last Name', 'required': True }),
        'phonenumber': forms.TextInput(attrs={ 'class': 'form-control', 'placeholder':'Phone Number', 'required': True }),
        'email': forms.EmailInput(attrs={ 'class': 'form-control', 'placeholder':'Email','required': False }),
        'location': forms.TextInput(attrs={ 'class': 'form-control' , 'placeholder':'Location', 'required': True }),
        }
        labels = {
            'reg_date': 'Date',
            'firstname': 'First Name',
            'lastname': 'Last Name',
            'phonenumber': 'Phone Number',
            'email': 'Email',
            'location': 'Location',
        }

class SalesForm(forms.ModelForm):
    #product= forms.ModelChoiceField(LayersProducts.objects.all(),empty_label="(Nothing)")

    class Meta:
        model=LayersSales
        fields=['date','enterprise_type','section','customer','product','paymentmode','quantity','unitprice','staff']
        widgets={
        'date': forms.DateInput(attrs={'class': 'form-control text-input text-muted','type': 'date','required': True}, format='%Y-%m-%d'),
        'enterprise_type': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Enterprise Type', 'required': True}),
        'section': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Enterprise Unit','required': True }),
        'customer': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Customer', 'required': True }),
        'product': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Product','required': True }),
        'paymentmode': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Payment Mode', 'required': True }),
        'quantity': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Quantity', 'required': True }),
        'unitprice': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Unit Price', 'required': True }),
        'staff': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Sales Person', 'required': True }),
        }
        labels={
        'date': 'Date',
        'enterprise_type':'Business',
        'section':'Enterprise Unit',
        'customer':'Customer',
        'product':'Product',
        'paymentmode':'Payment Mode',
        'quantity':'Quantity',
        'unitprice':'Unit Price',
        'staff':'Sales Person',
        }
    def __init__(self, *args, **kwargs):
        super(SalesForm, self).__init__(*args, **kwargs)
        self.fields['enterprise_type'].empty_label='Enterprise Type'
        self.fields['section'].empty_label='Enterprise Unit'
        self.fields['customer'].empty_label='Customer'
        self.fields['product'].empty_label='Product'
        self.fields['paymentmode'].empty_label='Payment Method'
        self.fields['staff'].empty_label='Sales Person'

class ProductionForm(forms.ModelForm):
    class Meta:
        model = LayersProduction
        #fields = "__all__"
        fields = ['prod_date','enterprise_type','section','gross', 'defects','broken','staff']
        widgets = {
        'prod_date': forms.DateInput(attrs={'class': 'form-control text-input text-muted','type': 'date','required': True}, format='%Y-%m-%d'),
        'enterprise_type': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Enterprise Type', 'required': True}),
        'section': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Enterprise Unit','required': True }),
        'gross': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Gross Production', 'required': True }),
        'defects': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Defective Eggs', 'required': True }),
        'broken': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Broken Eggs', 'required': True }),
        'staff': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Staff', 'required': True }),

        }
        labels = {
        'prod_date': 'Date',
        'enterprise_type':'Business',
        'section':'Enterprise Unit',
        'gross':'Gross Production',
        'defects':'Defective Eggs',
        'broken':'Broken Eggs',
        'staff':'Staff',

        }

    def __init__(self, *args, **kwargs):
        super(ProductionForm, self).__init__(*args, **kwargs)
        self.fields['enterprise_type'].empty_label='Enterprise Type'
        self.fields['section'].empty_label='Enterprise Unit'
        self.fields['staff'].empty_label='Collector'

class BirdsInventoryForm(forms.ModelForm):
    class Meta:
        model = LayersStockMovement
        fields = ['stock_date','enterprise_type','section','stock_movement_type', 'stock_movement_reason','birds','birds_stock_actual','stock_movement_notes','staff']
        widgets = {
        'stock_date': forms.DateInput(attrs={'class': 'form-control text-input text-muted','type': 'date','required': True}, format='%Y-%m-%d'),
        'enterprise_type': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Enterprise Type', 'required': True}),
        'section': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Enterprise Unit','required': True }),
        'stock_movement_type': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Type', 'required': True }),
        'stock_movement_reason': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Reason','required': True }),
        'birds': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Number of Birds', 'required': True }),
        'birds_stock_actual': forms.NumberInput(attrs={ 'class': 'form-control text-muted inputstatus' , 'placeholder':'Stock Count', 'required': False}),
        'stock_movement_notes': forms.TextInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Remarks', 'required': False }),
        'staff': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Stock Taker', 'required': True }),

        }
        labels = {
        'stock_date': 'Date',
        'enterprise_type':'Business',
        'section':'Enterprise Unit',
        'stock_movement_type':'Type of Movement',
        'stock_movement_reason':'Reason',
        'birds':'Number of Birds',
        'stock_movement_notes':'Remarks',
        'birds_stock_actual':'Actual Stock Count',
        'staff':'Stock Taker',

        }

    def __init__(self, *args, **kwargs):
        super(BirdsInventoryForm, self).__init__(*args, **kwargs)
        self.fields['enterprise_type'].empty_label='Enterprise Type'
        self.fields['section'].empty_label='Enterprise Unit'
        self.fields['stock_movement_type'].empty_label='Type of Movement'
        self.fields['stock_movement_reason'].empty_label='Reason of Movement'
        self.fields['birds_stock_actual'].empty_label='Stock Count'
        self.fields['staff'].empty_label='Stock Taker'


class EggsInventoryForm(forms.ModelForm):
    class Meta:
        model = LayersEggsInventory
        fields = ['stock_date','enterprise_type','section','egg_loss_defects','egg_loss_breakages','egg_loss_unaccounted','eggs_stock_actual_crates','eggs_stock_actual_pieces','staff']
        widgets = {
        'stock_date': forms.DateInput(attrs={'class': 'form-control text-input text-muted','type': 'date','required': True}, format='%Y-%m-%d'),
        'enterprise_type': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Enterprise Type', 'required': True}),
        'section': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Enterprise Unit','required': True }),
        'egg_loss_defects': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Defects', 'required': True }),
        'egg_loss_breakages': forms.NumberInput(attrs={ 'class': 'form-control text-muted disabled_input' , 'placeholder':'Broken', 'required': True}),
        'egg_loss_unaccounted': forms.NumberInput(attrs={ 'class': 'form-control text-muted disabled_input' , 'placeholder':'Unaccounted', 'required': True}),
        'eggs_stock_actual_crates': forms.NumberInput(attrs={ 'class': 'form-control text-muted inputstatus' , 'placeholder':'Crates', 'required': True}),
        'eggs_stock_actual_pieces': forms.NumberInput(attrs={ 'class': 'form-control text-muted inputstatus' , 'placeholder':'Pieces', 'required': True}),
        'staff': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Stock Taker', 'required': True }),
        }

        labels = {
        'stock_date': 'Date',
        'enterprise_type':'Business',
        'section':'Enterprise Unit',
        'egg_loss_defects':'Defects',
        'egg_loss_breakages':'Broken',
        'egg_loss_unaccounted':'Unaccounted',
        'eggs_stock_actual_crates':'Crates',
        'eggs_stock_actual_pieces':'Crates',
        'staff':'Stock Taker',

        }

    def __init__(self, *args, **kwargs):
        super(EggsInventoryForm, self).__init__(*args, **kwargs)
        self.fields['enterprise_type'].empty_label='Enterprise Type'
        self.fields['section'].empty_label='Enterprise Unit'
        self.fields['egg_loss_defects'].empty_label='Defects'
        self.fields['egg_loss_breakages'].empty_label='Breakages'
        self.fields['egg_loss_unaccounted'].empty_label='Unaccounted/Stolen'
        self.fields['eggs_stock_actual_crates'].empty_label='Crates'
        self.fields['eggs_stock_actual_pieces'].empty_label='Pieces'
        self.fields['staff'].empty_label='Stock Taker'


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = LayersExpenses
        fields = ['purchase_date','enterprise_type','section','cost_category','vendor','expense_details','quantity','unitprice','paymentmode','cashpoint','staff']
        widgets = {
        'purchase_date': forms.DateInput(attrs={'class': 'form-control text-input text-muted','type': 'date','required': True}, format='%Y-%m-%d'),
        'enterprise_type': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Enterprise Type', 'required': True}),
        'section': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Enterprise Unit','required': True }),
        'cost_category': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Type of Expense', 'required': True }),
        'vendor': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Vendor', 'required': False }),
        'expense_details': forms.TextInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Details', 'required': True }),
        'quantity': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Quantity', 'required': True}),
        'unitprice': forms.NumberInput(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Unit Price', 'required': True}),
        'paymentmode': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Payment Mode', 'required': False }),
        'cashpoint': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Payment Point', 'required': False }),
        'staff': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Staff', 'required': True }),
        }

        labels = {
        'stock_date': 'Date',
        'enterprise_type':'Business',
        'section':'Enterprise Unit',
        'cost_category':'Type of Expense',
        'vendor':'Vendor',
        'expense_details':'Details',
        'quantity':'Quantity',
        'unitprice':'Unit Price',
        'paymentmode':'Payment Mode',
        'cashpoint':'Payment Point',
        'staff':'Staff',
        }

    def __init__(self, *args, **kwargs):
        super(ExpensesForm, self).__init__(*args, **kwargs)
        self.fields['enterprise_type'].empty_label='Enterprise Type'
        self.fields['section'].empty_label='Enterprise Unit'
        self.fields['staff'].empty_label='Staff'
        self.fields['vendor'].empty_label='Vendor'
        self.fields['cost_category'].empty_label='Expense Type'
        self.fields['paymentmode'].empty_label='Payment Mode'
        self.fields['cashpoint'].empty_label='Payment Mode'


class DepositForm(forms.ModelForm):
    class Meta:
        model = LayersCashDeposit
        fields = ['deposit_date','enterprise_type','section','cashpoint','cash_balance','deposit_amount','staff']
        widgets = {
        'deposit_date': forms.DateInput(attrs={'class': 'form-control text-input text-muted','type': 'date','required': True}, format='%Y-%m-%d'),
        'enterprise_type': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Enterprise Type', 'required': True}),
        'section': forms.Select(attrs={ 'class': 'form-control text-muted', 'placeholder':'Enterprise Unit','required': True }),
        'cash_balance': forms.NumberInput(attrs={ 'class': 'form-control text-muted disabled_input' , 'placeholder':'Cash Balance', 'required': True}),
        'deposit_amount': forms.NumberInput(attrs={ 'class': 'form-control text-muted  inputstatus' , 'placeholder':'Deposit Amount', 'required': False}),
        'cashpoint': forms.Select(attrs={ 'class': 'form-control text-muted  inputstatus' , 'placeholder':'Deposit Point', 'required': False }),
        'staff': forms.Select(attrs={ 'class': 'form-control text-muted' , 'placeholder':'Depositor', 'required': True }),
        }

        labels = {
        'stock_date': 'Date',
        'enterprise_type':'Business',
        'section':'Enterprise Unit',
        'cash_balance':'Cash Balance',
        'deposit_amount':'Deposit Amount',
        'cashpoint':'Payment Point',
        'staff':'Staff',
        }

    def __init__(self, *args, **kwargs):
        super(DepositForm, self).__init__(*args, **kwargs)
        self.fields['enterprise_type'].empty_label='Enterprise Type'
        self.fields['section'].empty_label='Enterprise Unit'
        self.fields['staff'].empty_label='Staff'
        self.fields['cashpoint'].empty_label='Deposit Point'
