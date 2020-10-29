from django.db import models
# from enterprise.models import Enterprise
# from enterprise.models import EnterpriseType
# from enterprise.models import Staff
# from enterprise.models import PaymentModes

#1 units
class LayersSection(models.Model):
    section=models.CharField(max_length=255)
    sub_section=models.CharField(max_length=255,blank=True, null=True)
    sub_sub_section=models.CharField(max_length=255,blank=True, null=True)
    # products=models.CharField(max_length=255)
    #category=models.ForeignKey(EnterpriseType, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Layers Units"
    def __str__(self):
        return '%s-%s' %  (self.unit,self.sub_section)


#2 products
class LayersProducts(models.Model):
    product=models.CharField(max_length=255)
    unit_measure=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="Layers Products"
    def __str__(self):
        return '%s %s' %  (self.product,self.unit_measure)

#3 Birds Inventory

class LayersInventory(models.Model):
    stock_date=models.DateField()
    #enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE)
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)
    stock_in =models.IntegerField()
    stock_out =models.IntegerField()
    stock_movement_type=models.CharField(max_length=255)
    stock_movement_notes=models.CharField(max_length=255)
    #staff=models.ForeignKey('enterprise.Staff', verbose_name="staff", on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Layers Inventory"

    def stock_date_1(self):
        return self.prod_date.strftime('%e %b %y')

    def stock_balance(self):
        stock_balance=self.stock_in-self.stock_out
        return stock_balance

#4 Daily production

class LayersProduction(models.Model):
    prod_date=models.DateField()
    #enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE)
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)
    birds=models.IntegerField()
    gross=models.IntegerField()
    defects=models.IntegerField()
    broken=models.IntegerField()
    #staff=models.ForeignKey('enterprise.Staff', verbose_name="staff", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural="Layers Production"

    def prod_date_1(self):
        return self.prod_date.strftime('%e %b %y')

    def nett(self):
        nett=self.gross-self.defects-self.broken
        return nett

    def gross_percentage(self):
        gross_percentage=self.gross/self.birds
        return gross_percentage

    def nett_percentage(self):
        nett_percentage=(self.gross-self.defects-self.broken)/self.birds
        return nett_percentage

#5 Cutomers

class LayersCustomers(models.Model):
    reg_date=models.DateField()
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=10)
    email=models.EmailField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True)

    def reg_date_2(self):
        return self.reg_date.strftime('%d %b %y')

    def reg_date_1(self):
        return self.reg_date.strftime('%F')

    def customername(self):
        return self.firstname + " " + self.lastname

    def __str__(self):
        return '%s %s' %  (self.firstname,self.lastname)

    class Meta:
        #db_table="customers_customers"
        ordering=["-reg_date"]
        verbose_name_plural="Layers Customers"


#6 Sales
class LayersSales(models.Model):
    date=models.DateField()
    #enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE)
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)
    customer=models.ForeignKey(LayersCustomers, verbose_name="customer", on_delete=models.CASCADE)
    product=models.ForeignKey(LayersProducts, verbose_name="product", on_delete=models.CASCADE)
    #paymentmode=models.ForeignKey('enterprise.PaymentModes', verbose_name="payment_mode", on_delete=models.CASCADE)
    #customer=models.CharField(max_length=255)
    #phonenumber=models.CharField(max_length=255)
    #email=models.EmailField(max_length=255, blank=True, null=True)
    #location=models.CharField(max_length=255, blank=True, null=True)
    #product=models.CharField(max_length=255)
    #salesperson=models.CharField(max_length=255)
    #paymentmode=models.CharField(max_length=255)
    #unitmeasure=models.CharField(max_length=255)
    quantity=models.IntegerField()
    unitprice=models.DecimalField(max_digits=5, decimal_places=2)
    #staff=models.ForeignKey('enterprise.Staff', verbose_name="staff", on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Layers Sales"

    def total(self):
        total= self.quantity*self.unitprice
        return total

    def date1(self):
        return self.date.strftime('%d %b %y')

    def __str__(self):
        return self.customer



#7 Expenses



#8 Vendors
