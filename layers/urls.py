from django.urls import path
from . import views


urlpatterns = [
    path('',views.layers_dashboard, name='layers_dashboard'),


    path('layers_customers/',views.layers_customers, name='layers_customers'),
    path('add_layers_customer/',views.add_layers_customer,name='add_layers_customer'),#in use
    path('edit_layers_customer/<int:id>',views.edit_layers_customer,name='edit_layers_customer'),#in use for modal
    #path('save_layers_customer/<int:id>',views.save_layers_customer,name='save_layers_customer'),#in use
    path('update_layers_customer/<int:id>',views.update_layers_customer,name='update_layers_customer'),#in use for non modal
    path('delete_layers_customer/<int:id>',views.delete_layers_customer,name='delete_layers_customer'),#in use for both modal and non-modal


    path('layers_sales/',views.layers_sales,name='layers_sales'),
    path('add_layers_sales/',views.add_layers_sales,name='add_layers_sales'),

    path('layers_expenses/',views.layers_expenses,name='layers_expenses'),
    path('add_layers_expenses/',views.add_layers_expenses,name='add_layers_expenses'),

    path('layers_production/',views.layers_production,name='layers_production'),
    path('add_layers_production/',views.add_layers_production,name='add_layers_production'),

    path('layers_birds_inventory/',views.layers_birds_inventory,name='layers_birds_inventory'),
    path('add_layers_stock_movement/',views.add_layers_stock_movement,name='add_layers_stock_movement'),

    path('layers_eggs_inventory/',views.layers_eggs_inventory,name='layers_eggs_inventory'),
    path('add_layers_eggs_inventory/',views.add_layers_eggs_inventory,name='add_layers_eggs_inventory'),

    path('layers_cash_flow/',views.layers_cash_flow,name='layers_cash_flow'),
    path('add_layers_cash_deposit/',views.add_layers_cash_deposit,name='add_layers_cash_deposit'),


    # path('layers_production/',views.layers_production, name='layers_production'),
    # path('layers_inventory/',views.layers_inventory, name='layers_inventory'),
]
