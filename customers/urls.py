from django.urls import path
from . import views
#from customers.views import CustomersList, CustomerDelete

urlpatterns = [
    #Function based views:
    #path('',views.customers, name='customers'),
    path('postcustomer/',views.postcustomer, name='postcustomer'),
    path('editcustomer/<str:id>',views.editcustomer,name='editcustomer'),
    path('updatecustomer/<str:id>',views.updatecustomer,name='updatecustomer'),#in use
    #path('deletecustomer/<str:id>',views.deletecustomer,name='deletecustomer'),
    path('customerdelete/<str:id>',views.customerdelete,name='customerdelete'),
    path('createcustomer/',views.createcustomer,name='createcustomer'),
    path('addcustomer/',views.addcustomer,name='addcustomer'),
    path('',views.add_customer_modal,name='add_customer_modal'),#in use
    path('<str:id>',views.update_customer_modal,name='update_customer_modal'),
    path('',views.save_customer_update,name='save_customer_update'),

    path('customeredit/<str:id>',views.customeredit,name='customeredit'),
    path('customerupdate/<str:id>',views.customerupdate,name='customerupdate'),
    path('<str:id>',views.delete_customer_modal,name='delete_customer_modal'),

    #Class based views:
    path('',views.CustomersList.as_view(), name='customers'),#in use
    path('customeradd/',views.CustomerAdd.as_view(), name='customeradd'),
    path('customerdetails/<str:id>',views.CustomerDetails.as_view(), name='customerdetails'),
    path('customer_update/<str:id>',views.CustomerUpdate.as_view(), name='customer_update'),
    path('deletecustomer/<str:id>',views.CustomerDelete.as_view(),name='deletecustomer'),#in use
    #path('customerview/<str:id>',views.CustomerView.as_view(), name='customerview'),

]
