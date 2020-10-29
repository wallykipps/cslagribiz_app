from django.contrib import admin

from .models import Sales


class SalesAdmin(admin.ModelAdmin):
    list_display= ('id','date','customer','phonenumber','location','product','salesperson','paymentmode','unitmeasure','units','unitprice')
    list_display_links = ('id', 'customer','product','salesperson')
    search_fields = ('customer','phonenumber','location','product','salesperson','paymentmode')
    list_per_page = 25

admin.site.register(Sales,SalesAdmin)
