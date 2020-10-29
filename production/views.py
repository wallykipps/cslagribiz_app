from django.shortcuts import render, redirect
# from .models import LayersProduction
# from .models import LayersInventory


def production_dashboard(request):
    return render (request, 'dashboard/production_dashboard.html')

def layersproduction(request):
    layers_production=LayersProduction.objects
    return render (request, 'production/layers_production.html',{'layers_production':layers_production})

def layers_inventory(request):
    layers_inventory=LayersInventory.objects
    return render (request, 'production/layers_inventory.html',{'layers_inventory':layers_inventory})
