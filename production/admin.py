from django.contrib import admin

# from .models import LayersProducts
# from .models import LayersSection
# from .models import LayersProduction
# from .models import LayersInventory
# from .models import LayersCustomers
# from .models import LayersSales

# class FarmAdmin(admin.ModelAdmin):
#     list_display= ('id','farm_name','location','farm_unit','farm_sub_unit')
#     list_display_links = ('id', 'farm_name')
#     search_fields = ('farm_name','location','farm_unit','farm_sub_unit')
#     list_per_page = 25

class LayersSectionAdmin(admin.ModelAdmin):
    list_display= ('id','section','sub_section','sub_sub_section')
    list_display_links = ('id','section')
    search_fields = ('section','sub_section')
    list_per_page = 25

class LayersCustomersAdmin(admin.ModelAdmin):
    list_display= ('id','reg_date','firstname','lastname','phonenumber','location','email')
    list_display_links = ('id','firstname','lastname')
    search_fields = ('firstname','lastname','phonenumber','location','email')
    list_per_page = 25


admin.site.register(LayersProducts)
admin.site.register(LayersSection, LayersSectionAdmin)
admin.site.register(LayersProduction)
admin.site.register(LayersInventory)
admin.site.register(LayersCustomers,LayersCustomersAdmin)
admin.site.register(LayersSales)
