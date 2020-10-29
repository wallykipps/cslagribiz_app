from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Customers
from .forms import customerForm
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView, CreateView, UpdateView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class CustomerView(FormView):
    template_name = 'contact.html'
    form_class = customerForm
    success_url = '/customers/'

    def form_valid(self, form):
        return super().form_valid(form)


class CustomersList(ListView):#working
    model = Customers
    #paginate_by = 3
    queryset = Customers.objects
    template_name='customers/customers.html'
    context_object_name="customers"

class CustomerAdd(CreateView):#working but not on modal
    model = Customers
    form_class=customerForm
    template_name = 'customers/addcustomer1.html'
    success_url = reverse_lazy('customers')
    #queryset=Customers.objects.all()
    #success_url = ('customers/customers')
    #fields = ['reg_date','firstname','lastname','phonenumber', 'email','location']

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CustomerDetails(DetailView):#not working
    model = Customers
    template_name='customers/customerdetails.html'
    fields = ['reg_date','firstname','lastname','phonenumber', 'email','location']
    success_url = reverse_lazy('customers')

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Customers, id=id_)


class CustomerUpdate(UpdateView):#not working
    model = Customers
    template_name='customers/editcustomer.html'
    fields = ['reg_date','firstname','lastname','phonenumber', 'email','location']

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Customers, id=id_)


class CustomerDelete(DeleteView):#working but not on modal
        model = Customers
        template_name='customers/deletecustomer.html'
        context_object_name="customer"
        success_url = reverse_lazy('customers')

        def get_object(self):
            id_=self.kwargs.get("id")
            return get_object_or_404(Customers, id=id_)

        #def get_success_url(self):
            #return reverse('customers')

def customers(request):
    customers=Customers.objects
    print(customers)
    return render(request,'customers/customers.html',{'customers':customers})

def postcustomer(request):
    #print(request.method)
    if(request.method)=="POST":
        #print("Sucess!")
        reg_date=request.POST.get("date")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        phonenumber=request.POST.get("phonenumber")
        location=request.POST.get("location")
        email=request.POST.get("email")
        print(reg_date,firstname,lastname,phonenumber,location,email)
        customerrecord=Customers(reg_date=reg_date,firstname=firstname,lastname=lastname,phonenumber=phonenumber,location=location,
        email=email)
        customerrecord.save()
        return redirect('customers')


# def editcustomer1(request,id):
#     print(request.method)
#     if request.method == 'GET'and request.is_ajax():
#         customer = Customers.objects.get(id=id)
#         print("Success!")
#         print(customer.id)
#         return redirect('customers')

def editcustomer(request, id):
    customer = Customers.objects.get(id=id)
    return render (request, 'customers/editcustomer.html',{'customer':customer})

def updatecustomer(request,id):
    customer = Customers.objects.get(id=id)
    if(request.method)=="POST":
        #print("Sucess!")
        customer.reg_date=request.POST.get("date")
        customer.firstname=request.POST.get("firstname")
        customer.lastname=request.POST.get("lastname")
        customer.phonenumber=request.POST.get("phonenumber")
        customer.location=request.POST.get("location")
        customer.email=request.POST.get("email")
        #print(customer.reg_date,customer.firstname,customer.lastname,customer.phonenumber,customer.location,customer.email,customer.customername)
        #print(customer)
        customer.save()
        return redirect('customers')



def deletecustomer(request, id):
    customer = Customers.objects.get(id=id)
    customer.delete()
    customers=Customers.objects
    #return redirect('customers')
    return render (request, 'customers/customers.html',{'customers': customers,'customer':customer})

def customerdelete(request, id):
    if(request.method)=="POST":
        customer = Customers.objects.get(id=id)
        print('Success!')
        customer.delete()
        return redirect('customers')

#CRUD using Model Forms
#Create customer - normal form
def createcustomer(request):
    form = customerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('customers')
    else:
         form = customerForm()
    return render (request, 'customers/addcustomer.html',{'form':form})

def addcustomer(request):
    form = customerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('customers')
    else:
        form = customerForm()
        return render (request, 'customers/addcustomer.html',{'form':form})

#Create customer - modal - in use
def add_customer_modal(request):
    form = customerForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('customers')
    else:
        form=customerForm()
        customers=Customers.objects
        return render (request, 'customers/customers.html',{'customers': customers,'form':form})

#Editcustomer - modal
def update_customer_modal(request,id):
    customer = Customers.objects.get(id=id)
    date=customer.reg_date
    firstname = customer.firstname
    lastname=customer.lastname
    phonenumber=customer.phonenumber
    email=customer.email
    location=customer.location
    context={'reg_date':date,'firstname': firstname, 'lastname':lastname, 'phonenumber':phonenumber,
    'email': email, 'location': location }
    print(context)
    #form = customerForm(instance=customer)
    #print(form)
    #return render (request, 'customers/customers.html',{'form':form})
    return JsonResponse(context)

    #return HttpResponse(form.as_p())

def save_customer_update(request):
    #customer = Customers.objects.get(id=id)
    print(request.method)
    if(request.method)=="POST":
        print("Sucess!")
        reg_date=request.POST.get("reg_date_update")
        firstname=request.POST.get("firstname_update")
        lastname=request.POST.get("lastname_update")
        phonenumber=request.POST.get("phonenumber_update")
        location=request.POST.get("location_update")
        email=request.POST.get("email_update")
        customer=Customers(reg_date=reg_date,firstname=firstname,lastname=lastname,phonenumber=phonenumber,location=location,
                email=email)
        print(reg_date,firstname,lastname,phonenumber,location,email)
        #print(customer)
        customer.save()
        return redirect('customers')



def delete_customer_modal(request, id):
    customer = Customers.objects.get(id=id)
    form = customerForm(instance=customer)
    print(form)
    if(request.method)=="POST":
        form = customerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    else:
        form=customerForm()
        customers=Customers.objects
        return render (request, 'customers/customers.html',{'customers': customers,'form':form})


#Update customer - modal
def customeredit(request, id):
    customer = Customers.objects.get(id=id)
    #customer =get_object_or_404(Customers, id=id)
    return render (request, 'customers/updatecustomer.html',{'customer':customer})

def customerupdate(request, id):
    customer = Customers.objects.get(id=id)
    #customer =get_object_or_404(Customers, id=id)
    form = customerForm(request.POST, instance=customer)
    if form.is_valid():
        print('success!')
        form.save()
        return redirect('customers')
    else:
        return render (request, 'customers/updatecustomer.html',{'customer':customer})
