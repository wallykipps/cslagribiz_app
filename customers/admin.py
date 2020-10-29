from django.contrib import admin

from .models import Customers

class CustomersAdmin(admin.ModelAdmin):
    list_display= ('id','reg_date','firstname','lastname','phonenumber','location','email')
    list_display_links = ('id','firstname','lastname')
    search_fields = ('firstname','lastname','phonenumber','location','email')
    list_per_page = 25

admin.site.register(Customers,CustomersAdmin)
