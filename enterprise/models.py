from django.db import models
#from django_pandas.managers import DataFrameManager

# Create your models here.


class Enterprise(models.Model):
    enterprise_name=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="Enterprises"
    def __str__(self):
        return '%s-%s' % (self.enterprise_name,self.branch)


class EnterpriseType(models.Model):
    type=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    sub_category=models.CharField(max_length=255)
    # products=models.CharField(max_length=255)
    enterprise=models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Enterprise Types"
    def __str__(self):
        return '%s-%s' %  (self.category,self.sub_category)


class Staff(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=255)
    enterprise=models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural="Staff"
    def __str__(self):
        return self.firstname
        #return '%s %s' %  (self.firstname,self.lastname)


class PaymentModes(models.Model):
    paymentmode=models.CharField(max_length=255)
    class Meta:
        verbose_name_plural="Payment Modes"
    def __str__(self):
        return self.paymentmode
