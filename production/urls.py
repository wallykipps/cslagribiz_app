from django.urls import path
from . import views


urlpatterns = [
    path('',views.production_dashboard, name='production_dashboard'),
    path('layersproduction/',views.layersproduction, name='layersproduction'),
    path('layers_inventory/',views.layers_inventory, name='layers_inventory'),
]
