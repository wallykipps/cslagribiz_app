from django.contrib import admin

from .models import Enterprise
from .models import EnterpriseType
from .models import Staff
from .models import PaymentModes


class EnterpriseAdmin(admin.ModelAdmin):
    list_display= ('id','enterprise_name','branch', 'location')
    list_display_links = ('id','enterprise_name')
    search_fields = ('enterprise_name','location','branch')
    list_per_page = 25


class EnterpriseTypeAdmin(admin.ModelAdmin):
    list_display= ('id','type','category','sub_category','enterprise')
    list_display_links = ('id','category')
    search_fields = ('unit','category','sub_category','products','enterprise')
    list_per_page = 25


class StaffAdmin(admin.ModelAdmin):
    list_display= ('id','firstname','lastname','phonenumber','enterprise')
    list_display_links = ('id', 'firstname')
    search_fields = ('firstname','sub_lastname')
    list_per_page = 25

class PaymentModesAdmin(admin.ModelAdmin):
    list_display= ('id','paymentmode')
    list_display_links = ('id', 'paymentmode')
    search_fields = ('id','paymentmode')
    list_per_page = 25

admin.site.register(Enterprise, EnterpriseAdmin)
admin.site.register(EnterpriseType,EnterpriseTypeAdmin)
admin.site.register(Staff,StaffAdmin)
admin.site.register(PaymentModes,PaymentModesAdmin)
