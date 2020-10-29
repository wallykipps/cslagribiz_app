from django.db import models
from django_pandas.managers import DataFrameManager
from django_pandas.io import read_frame
from django.urls import reverse
from enterprise.models import Enterprise
from enterprise.models import EnterpriseType
from enterprise.models import Staff
from enterprise.models import PaymentModes
from django.forms import ModelForm

#1 units
class LayersSection(models.Model):
    section=models.CharField(max_length=255)
    sub_section=models.CharField(max_length=255,blank=True, null=True)
    sub_sub_section=models.CharField(max_length=255,blank=True, null=True)
    class Meta:
        verbose_name_plural="Layers Units"
    def __str__(self):
        #return '%s-%s' %  (self.section,self.sub_section)
        return self.section


#2 products
class LayersProducts(models.Model):
    product=models.CharField(max_length=255)
    unit_measure=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="Layers Products"
    def __str__(self):
        return '%s (%s)' %  (self.product,self.unit_measure)


#3 Birds Inventory
class LayersStockMovement(models.Model):
    stock_date=models.DateField()
    enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE)
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)

    STOCK_MOVEMENT_TYPE_CHOICES = [
        ('', 'Type of Movement'),
        ('Stock In', 'Stock In'),
        ('Stock Out', 'Stock Out'),
        ]
    stock_movement_type = models.CharField(
        max_length=15,
        choices=STOCK_MOVEMENT_TYPE_CHOICES,
        default='',
    )

    STOCK_MOVEMENT_REASON_CHOICES = [
        ('', 'Reason'),
        ('Day Old Chicks', 'Day Old Chicks'),
        ('Mortality', 'Mortality'),
        ('Stolen', 'Stolen'),
        ('Unaccounted', 'Unaccounted'),
        ('Error Correction', 'Error Correction'),
        ]
    stock_movement_reason = models.CharField(
        max_length=15,
        choices=STOCK_MOVEMENT_REASON_CHOICES,
        default='',
    )
    birds =models.IntegerField()
    birds_stock_actual=models.IntegerField(blank=True)
    stock_movement_notes=models.CharField(max_length=255,blank=True)
    staff=models.ForeignKey('enterprise.Staff', verbose_name="staff", on_delete=models.CASCADE)
    objects = DataFrameManager()
    class Meta:
        ordering=["stock_date"]
        verbose_name_plural="Layers Birds Inventory"

    def stock_date_1(self):
        return self.stock_date.strftime('%e-%b-%y')

    def stock_balance(self):
        stock_balance=self.stock_in-self.stock_out
        return stock_balance

#4 Daily production

class LayersProduction(models.Model):
    prod_date=models.DateField()
    enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE)
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)
    gross=models.IntegerField()
    defects=models.IntegerField()
    broken=models.IntegerField()
    staff=models.ForeignKey('enterprise.Staff', verbose_name="staff", on_delete=models.CASCADE)
    objects = DataFrameManager()

    class Meta:
        ordering=["-prod_date"]
        verbose_name_plural="Layers Production"

    def prod_date_1(self):
        return self.prod_date.strftime('%e-%b-%y')

    def nett(self):
        nett=self.gross-self.defects-self.broken
        return nett

    def gross_crates(self):
        gross_crates=self.gross/30
        return gross_crates

    def nett_crates(self):
        nett_crates=(self.gross-self.defects-self.broken)/30
        return nett_crates

    def gross_percentage(self):
        gross_percentage=self.gross/self.birds
        return gross_percentage

    def nett_percentage(self):
        nett_percentage=(self.gross-self.defects-self.broken)/self.birds
        return nett_percentage

#3 Birds Inventory
class LayersEggsInventory(models.Model):
    stock_date=models.DateField()
    enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE)
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)
    # UNIT_CHOICES = [
    #     ('CRATES', 'Crates'),
    #     ('PIECES', 'Pieces'),
    #     ]
    # unit = models.CharField(
    #     max_length=15,
    #     choices=UNIT_CHOICES,
    #     default='PIECES',
    # )
    #
    # EGG_LOSS_CHOICES = [
    #     ('DEFECTS', 'Defects'),
    #     ('BREAKAGES', 'Breakages'),
    #     ('EXPIRED', 'Expired'),
    #     ('UNACCOUNTED', 'Unaccounted'),
    #     ]
    # loss_type = models.CharField(
    #     max_length=15,
    #     choices=EGG_LOSS_CHOICES,
    #     default='DEFECTS',
    # )
    # quantity_lost =models.IntegerField()
    egg_loss_defects=models.IntegerField()
    egg_loss_breakages=models.IntegerField()
    egg_loss_unaccounted=models.IntegerField()
    eggs_stock_actual_crates=models.IntegerField(null=True, blank=True)
    eggs_stock_actual_pieces=models.IntegerField(null=True, blank=True)
    staff=models.ForeignKey('enterprise.Staff', verbose_name="staff", on_delete=models.CASCADE)
    objects = DataFrameManager()
    class Meta:
        ordering=["stock_date"]
        verbose_name_plural="Layers Eggs Inventory"

    def stock_date_1(self):
        return self.stock_date.strftime('%e-%b-%y')

    def total_moved(self):
        if movement_type=='PIECES':
            total_moved=self.quantity_moved/30
        else:
            total_moved=self.quantity_moved
        return total_moved

    def egg_total_losses(self):
        egg_total_losses=egg_loss_defects+egg_loss_breakages+egg_loss_unaccounted
        return egg_total_losses

    def eggs_stock_actual(self):
        eggs_stock_actual=eggs_stock_actual_crates+(eggs_stock_actual_pieces/30)
        return eggs_stock_actual


#5 Cutomers

class LayersCustomers(models.Model):
    reg_date=models.DateField()
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=10)
    email=models.EmailField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True)
    objects = DataFrameManager()

    def reg_date_1(self):
        return self.reg_date.strftime('%F')

    def reg_date_2(self):
        return self.reg_date.strftime('%e-%b-%y')


    def customername(self):
        return self.firstname + " " + self.lastname

    def __str__(self):
        return '%s %s' %  (self.firstname,self.lastname)

    class Meta:
        db_table="layers_layerscustomers"
        ordering=["-reg_date"]
        verbose_name_plural="Layers Customers"

#6 Sales
class LayersSales(models.Model):
    date=models.DateField()
    enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE,related_name="Layers")
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)
    customer=models.ForeignKey(LayersCustomers, verbose_name="customer", on_delete=models.CASCADE)
    product=models.ForeignKey(LayersProducts, verbose_name="product", on_delete=models.CASCADE)
    paymentmode=models.ForeignKey('enterprise.PaymentModes', verbose_name="payment_mode", on_delete=models.CASCADE)
    quantity=models.IntegerField()
    unitprice=models.DecimalField(max_digits=5, decimal_places=2)
    staff=models.ForeignKey('enterprise.Staff', verbose_name="staff", on_delete=models.CASCADE)
    objects = DataFrameManager()
    class Meta:
        ordering=["-date"]
        verbose_name_plural="Layers Sales"


    def total_sales(self):
        total= self.quantity*self.unitprice
        return total

    def total_crates(self): # To be used for inventory calculation
        if self.product.unit_measure=='Pieces':
            total_crates=self.quantity/30
        else:
            total_crates=self.quantity
        return total_crates

    def date1(self):
        return self.date.strftime('%d-%b-%y')

    def enterprise_unit(self):
        return self.enterprise_type.sub_category

    def section_name(self):
        return self.section.section

    def product_type(self):
        return self.product.product

    def product_unit(self):
        return self.product.unit_measure

    def __str__(self):
        return '%s-%s-%s' %  (self.customer,self.paymentmode,self.quantity)


#7 Vendors
class LayersVendors(models.Model):
    vendor_date=models.DateField()
    vendor=models.CharField(max_length=255,blank=True, null=True)
    phonenumber=models.CharField(max_length=10,blank=True, null=True)
    email=models.EmailField(max_length=255, blank=True, null=True)
    location=models.CharField(max_length=255, blank=True)
    objects = DataFrameManager()

    class Meta:
        ordering=["-vendor_date"]
        verbose_name_plural="Layers Vendors"


    def vendor_date_1(self):
        return self.reg_date.strftime('%e-%b-%y')

    def __str__(self):
        return self.vendor

#8 Expenses Categories
class LayersCostCategories(models.Model):
    cost_category=models.CharField(max_length=255)

    class Meta:
        verbose_name_plural="Layers Cost Categories"

    def __str__(self):
        return self.cost_category

# Cash Points

class LayersCashPoints(models.Model):
    cash_type=models.CharField(max_length=255)
    cash_point=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="Layers Cash Points"
    def __str__(self):
        return '%s-%s' %  (self.cash_type,self.cash_point)



#9 Expenses

class LayersExpenses(models.Model):
    purchase_date=models.DateField()
    enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE)
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)
    cost_category=models.ForeignKey(LayersCostCategories, verbose_name="cost category", on_delete=models.CASCADE)
    vendor=models.ForeignKey(LayersVendors, verbose_name="vendor", on_delete=models.CASCADE,blank=True)
    expense_details=models.CharField(max_length=255)
    quantity=models.DecimalField(max_digits=10, decimal_places=2)
    unitprice=models.DecimalField(max_digits=10, decimal_places=2)
    staff=models.ForeignKey('enterprise.Staff', verbose_name="purchaser", on_delete=models.CASCADE)
    paymentmode=models.ForeignKey('enterprise.PaymentModes', verbose_name="payment_mode", on_delete=models.CASCADE)
    cashpoint=models.ForeignKey(LayersCashPoints, verbose_name="payment_point", on_delete=models.CASCADE)
    objects = DataFrameManager()

    class Meta:
        ordering=["-purchase_date"]
        verbose_name_plural="Layers Expenses"

    def total_cost(self):
        total= self.quantity*self.unitprice
        return total

    def purchase_date_1(self):
        return self.purchase_date.strftime('%e-%b-%y')


class LayersCashDeposit(models.Model):
    deposit_date=models.DateField()
    enterprise_type=models.ForeignKey('enterprise.EnterpriseType', verbose_name="enterprise_type", on_delete=models.CASCADE)
    section=models.ForeignKey(LayersSection, verbose_name="section", on_delete=models.CASCADE)
    cashpoint=models.ForeignKey(LayersCashPoints, verbose_name="deposit_point", on_delete=models.CASCADE)
    deposit_amount=models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    cash_balance=models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    staff=models.ForeignKey('enterprise.Staff', verbose_name="depositor", on_delete=models.CASCADE)
    objects = DataFrameManager()
    class Meta:
        ordering=["-deposit_date"]
        verbose_name_plural="Layers Deposit"

    def deposit_date_1(self):
        return self.deposit_date.strftime('%e-%b-%y')



class LayersCreditManagement(models.Model):
    installment_date=models.DateField()
    customer=models.ForeignKey(LayersSales, verbose_name="customer", on_delete=models.CASCADE)
    installment_amount=models.DecimalField(max_digits=10, decimal_places=2,blank=True, null=True)
    staff=models.ForeignKey('enterprise.Staff', verbose_name="depositor", on_delete=models.CASCADE)
    objects = DataFrameManager()

    class Meta:
        ordering=["-installment_date"]
        verbose_name_plural="Layers Credit Management"


    def installment_date_1(self):
        return self.installment_date.strftime('%e-%b-%y')
