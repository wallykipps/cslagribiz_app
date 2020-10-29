from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Sum, F, Q, Case, When, Window
from django.db.models.functions import Lead
import pandas as pd
import numpy as np
from django_pandas.io import read_frame
from .models import LayersCustomers
from .models import LayersSales
from .models import LayersExpenses
from .models import LayersProduction
from .models import LayersStockMovement
from .models import LayersEggsInventory
from .models import LayersCashDeposit
from .models import LayersCreditManagement
from .forms import CustomerForm
from .forms import SalesForm
from .forms import ProductionForm
from .forms import BirdsInventoryForm
from .forms import EggsInventoryForm
from .forms import ExpensesForm
from .forms import DepositForm
from enterprise.models import Staff

# from django.urls import reverse_lazy
# from django.views.generic.edit import DeleteView, CreateView, UpdateView, FormView
# from django.views.generic.list iSalesstView
# from django.views.generic.detail import DetailView

#1 display the layers dashboard
def layers_dashboard(request):
    return render (request, 'dashboard/home.html')

#2 Show the customers
def layers_customers(request):
    layers_customers=LayersCustomers.objects
    form=CustomerForm()
    #use of pandas
    df = layers_customers.to_dataframe()
    df['customer_name']=df['firstname']+" "+df['lastname']
    df_layers_customers = df.to_dict('records')
    #print(df_layers_customers)

    return render (request, 'layers/layers_customers.html',{'layers_customers':layers_customers,'df_layers_customers':df_layers_customers,'form':form})

#3 Create customer
def add_layers_customer(request):
    form = CustomerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('layers_customers')
    else:
        form=CustomerForm()
        layers_customers=LayersCustomers.objects
        return render (request, 'layers/layers_customers.html',{'layers_customers': layers_customers,'form':form})

#4 Edit and update Custoner
def edit_layers_customer(request, id):#For modal, in use
    customer = LayersCustomers.objects.get(id=id)
    # data={'reg_date': customer.reg_date, 'firstname': customer.firstname, 'lastname': customer.lastname,
    # 'phonenumber':customer.phonenumber,'email':customer.email, 'location':customer.location}
    # print(data)
    form = CustomerForm(request.POST or None, instance=customer)
    #print(form)
    if form.is_valid():
        print('success')
        form.save()
        return redirect('layers_customers')
    #return HttpResponse(form.as_table())
    #return JsonResponse(data)
    return render(request, 'layers/update_layers_customer_modal.html', {'form':form})

def update_layers_customer(request, id):#For non-modal. Not in use
    customer = LayersCustomers.objects.get(id=id)
    form = CustomerForm(request.POST or None, instance=customer)
    print(form)
    if form.is_valid():
        form.save()
        return redirect('layers_customers')
    return render(request, 'layers/update_layers_customer.html', {'form':form,'customer':customer})

#5 Delete Custoomer
def delete_layers_customer(request, id):
    customer = LayersCustomers.objects.get(id=id)
    if request.method=="POST":
        customer.delete()
        return redirect('layers_customers')
    return render(request, 'layers/delete_layers_customer.html', {'customer':customer})

#2 Show the customers
def layers_sales(request):
    layers_sales=LayersSales.objects
    sales_form=SalesForm()
    layers_credit_installments_data=LayersCreditManagement.objects.all()

    #df=layers_sales.to_dataframe()
    df=layers_sales.filter(paymentmode__paymentmode='Credit').to_dataframe()
    df['total']=df['quantity']*df['unitprice']
    df['customer_id']=df['id']
    df['installment_date']=0
    df['type']='Credit'
    df=df.filter(['customer_id','date','section','staff','customer','product','quantity','type','total','installment_amount'])
    print(df)



    #df1 = pd.DataFrame(layers_credit_installments_data)
    df1=layers_credit_installments_data.to_dataframe(['customer__id','installment_date','customer__section','customer__staff','customer__customer__firstname','customer__customer__lastname',
    'customer__paymentmode__paymentmode','customer__product','customer__quantity','customer__unitprice','installment_amount','staff'])
    df1['customer']=df1['customer__customer__firstname']+' '+df1['customer__customer__lastname']
    df1['total']=0
    df1['type']='Installment'
    df1=df1.filter(['customer__id','installment_date','customer__section','staff','customer', 'customer__product','customer__quantity','type','total','installment_amount'])
    df1=df1.rename(columns={'customer__id':'customer_id','installment_date':'date','customer__section':'section','customer__product':'product','customer__quantity':'quantity'})
    print(df1)


    df2=df.append(df1)
    df2 = df2.sort_values(['section','customer','customer_id'], ascending=[False,False,True])#sort panda datafrane
    df2.loc[df2['total'].isnull(), 'total'] = 0
    df2.loc[df2['installment_amount'].isnull(), 'installment_amount'] = 0
    df2['credit_nett']=df2['total']-df2['installment_amount']
    df2['date'] = pd.to_datetime(df2['date']).dt.strftime('%e-%b-%y')
    df2=df2.filter(['customer_id','date','staff','section','customer','product','quantity','type','total','installment_amount','credit_nett'])
    df2['credit_nett'] = df2['credit_nett'].astype(int)
    df2=df2.groupby(['customer_id','date','staff','section','customer','product','quantity','total','installment_amount','type'],sort=False).sum().reset_index()
    df2['credit_balance'] = df2.groupby(['customer_id'],sort=False).credit_nett.cumsum()
    print(df2)
    credit_installments_data=df2.to_dict('records')

    context={
    'layers_sales':layers_sales,
    'sales_form':sales_form,
    'credit_installments_data':credit_installments_data,
    }



    return render (request, 'layers/layers_sales.html',context)

#6 Create and post sales
def add_layers_sales(request):
    sales_form = SalesForm(request.POST)
    print(sales_form)
    if sales_form.is_valid():
        print('success')
        sales_form.save()
        return redirect('layers_sales')
    else:
        sales_form=SalesForm()
        layers_sales=LayersSales.objects
        return render (request, 'layers/layers_sales.html',{'layers_sales': layers_sales,'sales_form':sales_form})


#7 Edit and update Sales


#8 Delete Sales


# Show production data
def layers_production(request):
    layers_production=LayersProduction.objects.all()
    production_form=ProductionForm()
    return render(request,'layers/layers_production.html', {'layers_production':layers_production, 'production_form':production_form})

#Add production data

def add_layers_production(request):
    production_form = ProductionForm(request.POST)
    if production_form.is_valid():
        production_form.save()
        return redirect('layers_production')
    else:
        production_form=ProductionForm()
        layers_production=LayersProduction.objects
        return render (request, 'layers/layers_production.html', {'layers_production':layers_production,'production_form':production_form})

# Birds inventory data
def layers_birds_inventory(request):
    birds_inventory_data=LayersStockMovement.objects.all()
    #birds_sales_data =LayersSales.objects.all()
    birds_sales_data =LayersSales.objects.all()
    birds_inventory_form=BirdsInventoryForm()

    # #annotate method
    # layers_birds_inventory1=LayersStockMovement.objects.select_related().order_by('stock_date').annotate(
    #         birds_stock_in = Sum(Case(When(stock_movement_type='Stock In', then=F('birds')),default=0)),
    #         birds_stock_out = Sum(Case(When(stock_movement_type='Stock Out', then=F('birds')),default=0)),
    #         birds_stock_cumulative = Sum(Case(When(stock_movement_type='Stock In', then=F('birds')),default=0)-Case(When(stock_movement_type='Stock Out', then=F('birds')),default=0)),
    #         #birds_stock_balance=Lead('birds_stock_cumulative', offset=1, default=None),
    # )

    #pandas method
    #birds inventory data
    df = birds_inventory_data.to_dataframe()
    df.loc[df['stock_movement_type'] == 'Stock In', 'birds_stock_in'] = df['birds']
    df.loc[df['stock_movement_type'] == 'Stock Out', 'birds_stock_out'] = df['birds']
    df.loc[df['birds_stock_in'].isnull(), 'birds_stock_in'] = 0
    df.loc[df['birds_stock_out'].isnull(), 'birds_stock_out'] = 0
    df['birds_stock_nett']=df['birds_stock_in']-df['birds_stock_out']
    df=df.filter(['stock_date','enterprise_type','section','stock_movement_reason','birds_stock_in','birds_stock_out','birds_stock_nett','birds_stock_actual','staff'])
    #print(df)

    #sales data for inventory
    df1=birds_sales_data.to_dataframe()
    df1 = df1.loc[(df1['product'] == "Laying birds (Birds)")]
    #df3=df2.filter(['date','enterprise_type','section','product','quantity','staff'])
    df1['stock_date']=df1['date']
    df1['stock_movement_reason']='Sales'
    df1['birds_stock_in']=0
    df1['birds_stock_out']=df1['quantity']
    df1['birds_stock_nett']=df1['birds_stock_in']-df1['birds_stock_out']
    df1=df1.filter(['stock_date','enterprise_type','section','stock_movement_reason','birds_stock_in','birds_stock_out','birds_stock_nett','birds_stock_actual','staff'])
    #df2 = df1.loc[(df1['product'] == "Laying birds (Birds)")|(df1['product'] == "Eggs (Crates)")] #OR condition
    #df2 = df1.loc[(df1['product'] == "Laying birds (Birds)")&(df1['customer'] == "Not Applicable")] #AND condition

    #append inventory and sale data
    df=df.append(df1)
    df = df.sort_values(['section','stock_date'], ascending=[False,True])#sort panda datafrane
    df=df.groupby(['section','stock_date','stock_movement_reason','staff'],sort=False).sum().reset_index()

    df2=df


    df['birds_stock_cumulative'] = df.groupby(['section'],sort=False).birds_stock_nett.cumsum()#function for calculating running balance
    df['birds_stock_variance']=df['birds_stock_cumulative']-df['birds_stock_actual']
    df['stock_date'] = pd.to_datetime(df['stock_date']).dt.strftime('%e-%b-%y')
    #print(df)
    #df = df.sort_values(['section','stock_date'], ascending=[False,True])#sort panda datafrane
    layers_inventory_queryset = df.to_dict('records')#convert panda datafrane to query

    df2=df2.loc[(df2['birds_stock_actual'] .notna())]    #print(df2)
    layers_stock_count=df2.to_dict('records')
    #print(queryset)

    context={
    'birds_inventory_data':birds_inventory_data,
    'birds_inventory_form':birds_inventory_form,
    #'layers_birds_inventory':layers_birds_inventory,
    'layers_inventory_queryset':layers_inventory_queryset,
    'layers_stock_count':layers_stock_count
    }
    return render(request,'layers/layers_birds_inventory.html', context)


def add_layers_stock_movement(request):
    birds_inventory_form = BirdsInventoryForm(request.POST)
    if birds_inventory_form.is_valid():
        birds_inventory_form.save()
        return redirect('layers_birds_inventory')
    else:
        birds_inventory_form = BirdsInventoryForm()
        layers_birds_inventory=LayersStockMovement.objects
        return render(request,'layers/layers_birds_inventory.html', {'layers_birds_inventory':layers_birds_inventory, 'birds_inventory_form':birds_inventory_form})

def layers_eggs_inventory(request):
    eggs_inventory_data=LayersEggsInventory.objects.all()
    eggs_sales_data =LayersSales.objects.all()
    eggs_production_data=LayersProduction.objects.all()
    eggs_inventory_form=EggsInventoryForm()

    df = eggs_inventory_data.to_dataframe()
    df['eggs_losses']=df['egg_loss_defects']+df['egg_loss_breakages']+df['egg_loss_unaccounted']
    eggs_losses_queryset=df.to_dict('records')
    df['stock_movement_type']='Losses'
    df=df[df['eggs_losses']>0]
    df['stock_out']=df['eggs_losses']
    df['stock_out']=df['stock_out']/30
    df=df.filter(['stock_date','section','staff','stock_movement_type','stock_out','eggs_stock_actual_crates','eggs_stock_actual_pieces'])
    #print(df)

    df1=eggs_production_data.to_dataframe()
    df1['nett_production']=df1['gross']-df1['defects']-df1['broken']
    df1['stock_movement_type']='Production'
    df1['stock_date']=df1['prod_date']
    df1['stock_in']=df1['nett_production']
    df1['stock_in']=df1['stock_in']/30
    df1=df1.filter(['stock_date','section','staff','stock_movement_type','stock_in'])
    #print(df1)

    df2=eggs_sales_data.to_dataframe()
    df2.loc[df2['product'] == "Eggs (Crates)", 'crates'] = df2['quantity']
    df2.loc[df2['product'] == "Eggs (Pieces)", 'pieces'] = df2['quantity']/30
    df2.loc[df2['crates'].isnull(), 'crates'] = 0
    df2.loc[df2['pieces'].isnull(), 'pieces'] = 0
    df2['stock_out']=df2['crates']+df2['pieces']
    df2=df2[df2['stock_out']>0]
    df2['stock_date']=df2['date']
    df2['stock_movement_type']='Sales'
    df2=df2.filter(['stock_date','section','staff','stock_movement_type','stock_out'])
    #print(df2)

    # df_empty=df.empty
    # print(df_empty)
    # if df_empty==False:
    #     print('Success')
    #     df=df.append(df1)
    #     df=df.append(df2)
    #
    # else:
    #     print('Empty')
    #     df=df1
    #     df=df1.append(df2)
    #     print(df)


    df=df.append(df1)
    df=df.append(df2)
    df = df.sort_values(['stock_date','section'], ascending=[True,False])#sort panda datafrane
    #print(df)
    df.loc[df['stock_in'].isnull(), 'stock_in'] = 0
    df.loc[df['stock_out'].isnull(), 'stock_out'] = 0
    df['stock_out']=df['stock_out'].round(2)
    df['stock_in']=df['stock_in'].round(2)
    df['eggs_stock_nett']=df['stock_in']-df['stock_out']
    df['stock_date'] = pd.to_datetime(df['stock_date']).dt.strftime('%e-%b-%y')
    df3=df
    df=df.groupby(['stock_date','section','staff','stock_movement_type'],sort=False).sum().reset_index()#grouping and aggregating by column
    df['eggs_stock_cumulative'] = df.groupby(['section'],sort=False).eggs_stock_nett.cumsum()#function for calculating running balance
    df['eggs_stock_cumulative']=df['eggs_stock_cumulative'].round(2)
    #print(df)

    df3=df3.groupby(['stock_date','section'],sort=False).sum().reset_index()#grouping and aggregating by column
    df3['eggs_stock_cumulative'] = df3.groupby(['section'],sort=False).eggs_stock_nett.cumsum()#function for calculating running balance
    df3['eggs_stock_cumulative']=df3['eggs_stock_cumulative'].round(2)
    df3=df3.filter(['stock_date','section','staff','eggs_stock_cumulative'])
    print(df3)



    eggs_inventory_queryset=df.to_dict('records')


    df4 = eggs_inventory_data.to_dataframe()
    #df4['eggs_stock_cumulative']=0
    df4 = df4.sort_values(['stock_date','section'], ascending=[True,False])#sort panda datafrane
    #print(df4)

    df4['eggs_stock_actual']=df4['eggs_stock_actual_crates']+df4['eggs_stock_actual_pieces']/30
    df4=df4.filter(['stock_date','section','staff','eggs_stock_actual'])
    print(df4)

    df4=df4.join(df3, lsuffix='_df4', rsuffix='_df3')
    df4=df4.filter(['stock_date_df4','section_df4','staff_df4','eggs_stock_cumulative','eggs_stock_actual'])

    df4['eggs_stock_actual']=df4['eggs_stock_actual'].round(2)
    df4['eggs_stock_variance']=df4['eggs_stock_cumulative']-df4['eggs_stock_actual']
    df4['eggs_stock_variance']=df4['eggs_stock_variance'].round(2)
    df4['stock_date_df4'] = pd.to_datetime(df4['stock_date_df4']).dt.strftime('%e-%b-%y')

    eggs_stock_reconciliation=df4.to_dict('records')


    context = {
    'eggs_losses_queryset':eggs_losses_queryset,
    'eggs_inventory_queryset':eggs_inventory_queryset,
    'eggs_inventory_form':eggs_inventory_form,
    'eggs_stock_reconciliation': eggs_stock_reconciliation,
    }
    return render(request,'layers/layers_eggs_inventory.html', context)

def add_layers_eggs_inventory(request):
    eggs_inventory_form = EggsInventoryForm(request.POST)
    if eggs_inventory_form.is_valid():
        eggs_inventory_form.save()
        return redirect('layers_eggs_inventory')
    else:
        eggs_inventory_form = EggsInventoryForm()
        layer_eggs_inventory=LayersEggsInventory.objects.all()
        return render(request,'layers/layers_eggs_inventory.html', {'layers_eggs_inventory':layers_eggs_inventory, 'eggs_inventory_form':eggs_inventory_form})


def layers_expenses(request):
    layers_expenses_data=LayersExpenses.objects.all()
    layers_expenses_form = ExpensesForm()

    df1=layers_expenses_data.to_dataframe()
    df1_split=df1['cashpoint'].str.split("-", n = 1, expand = True)#split a cobined field
    df1['cashpoint']=df1_split[1]#make a new seperate column in the dataframe
    df1['amount']=df1['quantity']*df1['unitprice']
    #df1['cash_out'].round(2)
    df1['date']=df1['purchase_date']
    df1['category']=df1['cost_category']
    df1=df1[df1['paymentmode']!='Credit']
    df1=df1.filter(['date','section','category','amount'])
    df1['month'] = pd.to_datetime(df1['date'])
    df1=df1.filter(['month','section','category','amount'])
    df1=df1.groupby(['section','category', pd.Grouper(key='month', freq='M')]).sum().reset_index()
    df1['amount']=df1['amount'].map('{:,.2f}'.format)
    print(df1)


    context={
    'layers_expenses_data':layers_expenses_data,
    'layers_expenses_form':layers_expenses_form,
    }
    return render(request,'layers/layers_expenses.html', context)

def add_layers_expenses(request):
    layers_expenses_form = ExpensesForm(request.POST)
    if layers_expenses_form.is_valid():
        layers_expenses_form.save()
        return redirect('layers_expenses')
    else:
        layers_expenses_form = ExpensesForm()
        layers_expenses_data=LayersExpenses.objects.all()
        context={
        'layers_expenses_form':layers_expenses_form,
        'layers_expenses_data':layers_expenses_data,
        }
        return render(request,'layers/layers_expenses.html', {context})


def layers_cash_flow(request):
    layers_deposit_data=LayersCashDeposit.objects.all()
    layers_deposit_form = DepositForm()
    layers_expenses_data=LayersExpenses.objects.all()
    layers_sales_data=LayersSales.objects.all()
    layers_credit_installments_data=LayersCreditManagement.objects.all()


    df=layers_sales_data.to_dataframe()
    df_split=df['product'].str.split(" ", n = 1, expand = True)#split a cobined field
    df['product']=df_split[0]#make a new seperate column in the dataframe
    df=df[df['paymentmode']!='Credit']
    df['type']='Cash Sales'
    df['cash_in']=df['quantity']*df['unitprice']
    df['category']=df['product']
    df=df.filter(['date','section','type','category','cash_in'])
    #print(df)


    df1=layers_expenses_data.to_dataframe()
    df1['type']='Expenses'
    df1_split=df1['cashpoint'].str.split("-", n = 1, expand = True)#split a cobined field
    df1['cashpoint']=df1_split[1]#make a new seperate column in the dataframe
    df1['cash_out']=df1['quantity']*df1['unitprice']
    #df1['cash_out'].round(2)
    df1['date']=df1['purchase_date']
    df1['category']=df1['cost_category']
    df1=df1[df1['paymentmode']!='Credit']
    df1=df1.filter(['date','section','type','category','cash_out'])
    #print(df1)

    df2=layers_deposit_data.to_dataframe()
    df2['type']='Deposit'
    df2['category']='N/A'
    df2_split=df2['cashpoint'].str.split("-", n = 1, expand = True)#split a cobined field
    df2['cashpoint']=df2_split[1]#make a new seperate column in the dataframe
    df2['date']=df2['deposit_date']
    #df2['deposit_amount'].round(2)
    df2=df2.filter(['date','section','type','category','deposit_amount'])
    #print(df2)

    df4=layers_credit_installments_data.to_dataframe(['customer__id','installment_date','customer__section','customer__staff','customer__customer__firstname','customer__customer__lastname',
    'customer__paymentmode__paymentmode','customer__product__product','customer__quantity','customer__unitprice','installment_amount','staff'])
    df4['customer']=df4['customer__customer__firstname']+' '+df4['customer__customer__lastname']
    df4['total']=0
    df4['type']='Credit Sales'
    df4=df4.filter(['installment_date','customer__section','customer__product__product','type','installment_amount'])
    df4=df4.rename(columns={'customer__id':'customer_id','installment_date':'date','customer__section':'section','customer__product__product':'category','installment_amount':'cash_in'})
    #print(df4)


    df3=df.append(df1)
    df3=df3.append(df2)
    df3=df3.append(df4)
    df3 = df3.sort_values(['date','section'], ascending=[True,False])#sort panda datafrane
    #df3=df3.groupby(['date','section','type','category'],sort=False).sum().reset_index()
    df3.loc[df3['cash_in'].isnull(), 'cash_in'] = 0
    df3.loc[df3['cash_out'].isnull(), 'cash_out'] = 0
    df3.loc[df3['deposit_amount'].isnull(), 'deposit_amount'] = 0
    df3['cash_nett']=df3['cash_in']-df3['cash_out']
    df3['cash_nett_actual']=df3['deposit_amount']-df3['cash_out']
    df3['date'] = pd.to_datetime(df3['date']).dt.strftime('%e-%b-%y')
    df3=df3.groupby(['date','section','type','category'],sort=False).sum().reset_index()
    df4=df3
    df3['cash_balance'] = df3.cash_nett.cumsum()#function for calculating running balance
    df3['cash_balance_actual'] = df3.cash_nett_actual.cumsum()#function for calculating running balance
    df3['deposit_balance']=df3['cash_balance']-df3['cash_balance_actual']
    df3=df3.replace(0,'')
    #print(df3)
    layers_cash_balance=df3.to_dict('records')


    df4['month'] = pd.to_datetime(df4['date'])
    df7=df4
    #df4 = df4.sort_values(['month'], ascending=[True])#sort panda datafrane
    df4=df4.filter(['month','section','type','category','cash_in','cash_out','deposit_amount','cash_nett','cash_nett_actual'])
    df4=df4.groupby(['section','type','category', pd.Grouper(key='month', freq='M')]).sum().reset_index()
    df4 = df4.sort_values(['month','type'], ascending=[True,True])#sort panda datafrane
    df4['month'] = pd.to_datetime(df4['month']).dt.strftime('%b-%y')
    df4['cash_balance'] = df4.cash_nett.cumsum()#function for calculating running balance
    df4['cash_balance_actual'] = df4.cash_nett_actual.cumsum()#function for calculating running balance
    df4['deposit_balance']=df4['cash_balance']-df4['cash_balance_actual']
    #print(df4)
    layers_cash_flow=df4.to_dict('records')

    df7=df7.filter(['month','section','type','cash_in','cash_out','deposit_amount','cash_nett','cash_nett_actual'])
    df7=df7.groupby(['section','type', pd.Grouper(key='month', freq='M')]).sum().reset_index()
    df7 = df7.sort_values(['month','type'], ascending=[True,False])#sort panda datafrane
    df7['month'] = pd.to_datetime(df7['month']).dt.strftime('%b-%y')
    df7['cash_balance'] = df7.cash_nett.cumsum()#function for calculating running balance
    df7['cash_balance_actual'] = df7.cash_nett_actual.cumsum()#function for calculating running balance
    df7['deposit_balance']=df7['cash_balance']-df7['cash_balance_actual']
    #print(df7)



    #Pivot table

    df5=df4
    df5 = df5[(df5.type.isin(['Expenses']))]

    df5=pd.crosstab(df5.category, df5.month, values=df5.cash_out, aggfunc='sum', margins=True, margins_name="Total", dropna=False).fillna(0)
    print(df5)
    #df5=pd.pivot_table(df5,index=['category'],columns=['month'],values=['cash_out'],aggfunc=np.sum,fill_value=0,margins=True)
    df5 = df5.applymap("{0:,.0f}".format)


    df6=df4
    print(df6)
    df6 = df6[(df6.type.isin(['Cash Sales']))]
    #df6=df6.pivot(index='category', columns='month', values=['cash_in'])
    #df6=df6.fillna(0)

    df6=pd.crosstab(df6.category, df6.month, values=df6.cash_in, aggfunc='sum',margins=True, margins_name="Total").fillna(0)
    print(df6)
    #df6=df6.fillna(0)

    #df6=pd.pivot_table(df6,index=['category'],columns=['month'],values=['cash_in'],aggfunc=np.sum,fill_value=0,margins=True,margins_name="Total")
    df6 = df6.applymap("{0:,.0f}".format)


    html1 = df5.to_html(classes=["table table-striped table-hover table-condensed table-bordered table-sm  text-right"])
    html2 = df6.to_html(classes=["table table-striped table-hover table-bordered table.thead-dark table-sm border"],formatters=None,table_id='myDatatable',justify='left')

    #print(df5)
    #print(html2)

    context={
    'layers_deposit_data':layers_deposit_data,
    'layers_deposit_form':layers_deposit_form,
    'layers_cash_balance':layers_cash_balance,
    'layers_cash_flow':layers_cash_flow,
    'html1':html1,
    'html2':html2
    }
    return render(request,'layers/layers_cash_recon.html', context)


def add_layers_cash_deposit(request):
    layers_deposit_form = DepositForm(request.POST)
    if layers_deposit_form.is_valid():
        layers_deposit_form.save()
        return redirect('layers_cash_flow')
    else:
        layers_deposit_form = DepositForm()
        layers_deposit_data=LayersExpenses.objects.all()
        context={
        'layers_deposit_data':layers_deposit_data,
        'layers_deposit_form':layers_deposit_form,
        }
        return render(request,'layers/layers_cash_recon.html', {context})




# def layers_inventory(request):
#     layers_inventory=LayersInventory.objects
#     return render (request, 'layers/layers_inventory.html',{'layers_inventory':layers_inventory})
