from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import LayersProducts
from .models import LayersSection
from .models import LayersProduction
from .models import LayersStockMovement
from .models import LayersEggsInventory
from .models import LayersCustomers
from .models import LayersSales
from .models import LayersVendors
from .models import LayersExpenses
from .models import LayersCashPoints
from .models import LayersCostCategories
from .models import LayersCashDeposit
from .models import LayersCreditManagement

class LayersSectionAdmin(admin.ModelAdmin):
#class LayersSectionAdmin(ImportExportModelAdmin):
    list_display= ('id','section','sub_section','sub_sub_section')
    list_display_links = ('id','section')
    search_fields = ('section','sub_section')
    list_per_page = 25

class LayersProductsAdmin(admin.ModelAdmin):
    list_display= ('id','product','unit_measure')
    list_display_links = ('id','product')
    search_fields = ('product','unit_measure')
    list_per_page = 25

class LayersCustomersAdmin(admin.ModelAdmin):
    list_display= ('id','reg_date','firstname','lastname','phonenumber','location','email')
    list_display_links = ('id','firstname','lastname')
    search_fields = ('firstname','lastname','phonenumber','location','email')
    list_per_page = 25

class LayersSalesAdmin(ImportExportModelAdmin):
    list_display=('id','date','enterprise_type','section','customer','product','paymentmode','quantity','unitprice','staff')
    list_display_links = ('id','enterprise_type','section','customer','product')
    search_fields = ('id','enterprise_type','section','customer','product')
    list_per_page = 25

class LayersCostCategoriesAdmin(admin.ModelAdmin):
    list_display=('id','cost_category')
    list_display_links = ('id','cost_category')
    search_fields = ('id','cost_category')
    list_per_page = 25

class LayersExpensesAdmin(ImportExportModelAdmin):
    list_display=('id','purchase_date','enterprise_type','section','cost_category','vendor','expense_details','paymentmode','cashpoint','quantity','unitprice','staff')
    list_display_links = ('id','enterprise_type','section','vendor','cost_category')
    search_fields = ('id','enterprise_type','section','vendor','cost_category')
    list_per_page = 25

class LayersCashPointsAdmin(admin.ModelAdmin):
    list_display=('id','cash_type','cash_point')
    list_display_links = ('id','cash_type','cash_point')
    search_fields = ('id','cash_type','cash_point')
    list_per_page = 25


class LayersVendorsAdmin(admin.ModelAdmin):
    list_display=('id','vendor_date','vendor','email','location')
    list_display_links = ('id','vendor')
    search_fields = ('id','vendor')
    list_per_page = 25

class LayersProductionAdmin(ImportExportModelAdmin):
    list_display=('id','prod_date','enterprise_type','section','gross','defects','broken','staff')
    list_display_links = ('id','section')
    search_fields = ('id','section')
    list_per_page = 25

class LayersStockMovementAdmin(ImportExportModelAdmin):
    list_display=('id','stock_date','enterprise_type','section','stock_movement_type','stock_movement_reason','birds','birds_stock_actual','stock_movement_notes','staff')
    list_display_links = ('id','section')
    search_fields = ('id','section')
    list_per_page = 25

class LayersEggsInventoryAdmin(ImportExportModelAdmin):
    list_display=('id','stock_date','enterprise_type','section','egg_loss_defects','egg_loss_breakages','egg_loss_unaccounted','eggs_stock_actual_crates','eggs_stock_actual_pieces','staff')
    list_display_links = ('id','section')
    search_fields = ('id','section')
    list_per_page = 25


class LayersCashDepositAdmin(ImportExportModelAdmin):
    list_display=('id','deposit_date','enterprise_type','section','cashpoint','cash_balance','deposit_amount','staff')
    list_display_links = ('id','section')
    search_fields = ('id','section')
    list_per_page = 25


class LayersCreditManagementAdmin(ImportExportModelAdmin):
    list_display=('id','installment_date','customer','installment_amount','staff')
    list_display_links = ('id','customer')
    search_fields = ('id','customer')
    list_per_page = 25
    list_filter = ('customer__paymentmode',)




admin.site.register(LayersProducts,LayersProductsAdmin)
admin.site.register(LayersSection, LayersSectionAdmin)
admin.site.register(LayersProduction,LayersProductionAdmin)
admin.site.register(LayersStockMovement,LayersStockMovementAdmin)
admin.site.register(LayersEggsInventory,LayersEggsInventoryAdmin)
admin.site.register(LayersCustomers,LayersCustomersAdmin)
admin.site.register(LayersSales,LayersSalesAdmin)
admin.site.register(LayersExpenses, LayersExpensesAdmin)
admin.site.register(LayersCashPoints, LayersCashPointsAdmin)
admin.site.register(LayersCostCategories, LayersCostCategoriesAdmin)
admin.site.register(LayersVendors,LayersVendorsAdmin)
admin.site.register(LayersCashDeposit,LayersCashDepositAdmin)
admin.site.register(LayersCreditManagement,LayersCreditManagementAdmin)
